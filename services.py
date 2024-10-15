from flask import render_template, redirect
from logic import is_admin, csrf_valid
import db


def edit_service(id, req):
    if not is_admin():
        return render_template("error.html", errmsg="You are not allowed to do that")
    if req.method == "GET":
        service = db.get_service(id)
        if not service:
            return render_template("error.html", errmsg="Could not find service")
        return render_template("edit_service.html", service=service)
    if req.method == "POST":
        if not csrf_valid(req):
            render_template("error.html", errmsg="Invalid Request")
        new_service = {}
        new_service["name"] = req.form.get("service_name")
        new_service["desc"] = req.form.get("service_desc")
        new_service["price"] = req.form.get("service_price")
        new_service["dur"] = req.form.get("service_dur")
        if db.edit_service(id, new_service):
            return redirect("/services")
        return render_template("error.html", errmsg="Could not update service")


def get_services(req):
    services = db.get_services()
    return render_template("services.html", services=services)
