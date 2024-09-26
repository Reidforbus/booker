from flask import session
import db


def is_admin():
    if session["username"]:
        return session["admin"]
    return False


def username_available(s):
    if " " in s:
        return False
    if s == "":
        return False
    if db.user_exists(s):
        return False
    return True
