from app import app
from db import db, get_services
import register
import login
import booking
from flask import redirect, render_template, request, session
from sqlalchemy.sql import text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def routelogin():
    return login.handlelogin(request)


@app.route("/logout")
def routelogout():
    del session["username"]
    del session["admin"]
    del session["user_id"]
    return redirect(request.referrer)


@app.route("/register", methods=["GET", "POST"])
def routeregister():
    return register.handleregister(request)


@app.route("/error")
def error(err="There was an error"):
    return render_template("error.html", errmsg=err)


@app.route("/products")
def routeservices():
    services = get_services()
    return render_template("products.html", products=services)


@app.route("/products/<int:id>/book", methods=["GET", "POST"])
def routebooking(id):
    if request.method == "GET":
        return booking.get_booking(request, id)
    return booking.book(request, id)
