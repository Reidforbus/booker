from flask import render_template, redirect
from logic import is_admin, csrf_invalid
import db


def get_service(id, req):
    service = db.get_service(id)
    if not service:
        return render_template("error.html", errmsg="Could not find service")
    return render_template("service.html", service=service)


def edit_service(id, req):
    if not is_admin():
        return render_template("error.html", errmsg="You are not allowed to do that")
    if req.method == "GET":
        service = db.get_service(id)
        if not service:
            return render_template("error.html", errmsg="Could not find service")
        return render_template("edit_service.html", service=service)
    if req.method == "POST":
        if csrf_invalid(req):
            render_template("error.html", errmsg="Invalid Request")
        new_service = {}
        new_service["name"] = req.form.get("service_name")
        new_service["desc"] = req.form.get("service_desc")
        new_service["price"] = req.form.get("service_price")
        new_service["dur"] = req.form.get("service_dur")
        if not valid_service(new_service):
            return render_template("error.html", errmsg="Invalid service details")
        if db.edit_service(id, new_service):
            return redirect(f"/services/{id}")
        return render_template("error.html", errmsg="Could not update service")


def get_services(req):
    services = db.get_services()
    return render_template("services.html", services=services)


def add_service(req):
    if not is_admin():
        return render_template("error.html", errmsg="You are not allowed to do that")
    if req.method == "GET":
        return render_template("add_service.html")
    if req.method == "POST":
        if csrf_invalid(req):
            render_template("error.html", errmsg="Invalid Request")
        new_service = {}
        new_service["name"] = req.form.get("service_name")
        new_service["desc"] = req.form.get("service_desc")
        new_service["price"] = req.form.get("service_price")
        new_service["dur"] = req.form.get("service_dur")
        if not valid_service(new_service):
            return render_template("error.html", errmsg="Invalid service details")
        new_id = db.add_service(new_service)
        if not new_id:
            return render_template("error.html", errmsg="Could not add new service")
        return redirect(f"/services/{new_id}")


def valid_service(service):
    if "name" not in service or service["name"] == "":
        return False
    if "desc" not in service or service["desc"] == "":
        return False
    if "price" not in service or int(service["price"]) < 0:
        return False
    if "dur" not in service or int(service["dur"]) % 20 != 0:
        return False
    return True
