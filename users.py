from flask import render_template, session
import db


def get_users(req):
    if "admin" not in session or not session["admin"]:
        return render_template("error.html", errmsg="You are not allowed to do that")
    users = db.get_users()
    return render_template("users.html", users=users)
