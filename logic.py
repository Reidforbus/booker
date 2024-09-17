from flask import session


def is_admin():
    if session["username"]:
        return session["admin"]
    return False
