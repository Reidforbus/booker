from flask import session, redirect, render_template
from db import get_user
from werkzeug.security import check_password_hash
from secrets import token_hex


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
        session["csrf_token"] = token_hex(16)
        return redirect(req.referrer)
    else:
        return render_template("error.html", errmsg="Incorrect login")
