from app import app
from db import get_services
from login import handlelogin, handlelogout
from register import handleregister
from booking import get_booking, book
from users import get_users
from service_calendar import get_calendar
from flask import render_template, request


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def routelogin():
    return handlelogin(request)


@app.route("/logout")
def routelogout():
    return handlelogout()


@app.route("/register", methods=["GET", "POST"])
def routeregister():
    return handleregister(request)


@app.route("/error")
def error(err="There was an error"):
    return render_template("error.html", errmsg=err)


@app.route("/services")
def routeservices():
    services = get_services()
    return render_template("services.html", services=services)


@app.route("/services/<int:id>/book", methods=["GET", "POST"])
def routebooking(id):
    if request.method == "GET":
        return get_booking(request, id)
    return book(request, id)


@app.route("/calendar")
def routecalendar():
    return get_calendar(request)


@app.route("/users")
def routeusers():
    return get_users(request)
