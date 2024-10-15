from flask import render_template
from logic import is_admin
import db


def get_users(req):
    if not is_admin():
        return render_template("error.html", errmsg="You are not allowed to do that")
    users = db.get_users()
    return render_template("users.html", users=users)
