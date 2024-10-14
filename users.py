from flask import render_template
import db


def get_users(req):
    users = db.get_users()
    return render_template("users.html", users=users)
