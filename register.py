from flask import session, render_template, redirect
import logic
from db import add_user


def handleregister(req):
    if req.method == "GET":
        if "username" in session:
            return render_template("error.html", errmsg="You are already logged in!")
        return render_template("register.html")
    username = req.form["username"]
    password = req.form["pwd"]
    valid, err = logic.username_available(username)
    if not valid:
        return render_template("error.html", errmsg=err)
    valid, err = logic.password_valid(password)
    if not valid:
        return render_template("error.html", errmsg=err)
    add_user(username, password, req.form["name"])
    return redirect("/")
