from flask import session, redirect, render_template
from db import get_user
from werkzeug.security import check_password_hash


def handlelogin(req):
    if req.method == "GET":
        return redirect("/")
    username = req.form["username"]
    password = req.form["pwd"]
    result = get_user(username)
    if result is None:
        return render_template("error.html", errmsg="Username does not exist")
    if check_password_hash(result.pwd, password):
        session["username"] = username
        session["admin"] = result.admin
        session["user_id"] = result.user_id
        return redirect(req.referrer)
    else:
        return render_template("error.html", errmsg="Incorrect login")
