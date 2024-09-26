from flask import session, render_template, redirect
import logic
from db import add_user


def handleregister(req):
    if req.method == "GET":
        if "username" in session:
            return render_template("error.html", errmsg="You are already logged in!")
        return render_template("register.html")
    username = req.form["username"]
    if not logic.username_available(username):
        return render_template("error.html", errmsg="username no good")
    add_user(username, req.form["pwd"], req.form["name"])
    return redirect("/")
