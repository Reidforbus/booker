from flask import session
import db


def is_admin():
    if "admin" in session:
        return session["admin"]
    return False


def username_available(s):
    if " " in s:
        return False, "Username cannot include whitespaces!"
    if s == "":
        return False, "Username cannot be empty!"
    if db.user_exists(s):
        return False, "Username is already taken."
    return True, ""


def password_valid(s):
    if " " in s:
        return False, "Password cannot include whitespaces!"
    if s == "":
        return False, "Password cannot be empty!"
    return True, ""


def csrf_invalid(req):
    return session["csrf_token"] != req.form.get("csrf_token")
