from app import app
from db import get_services
import register
import login
import booking
import service_calendar
from flask import redirect, render_template, request, session


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
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def routeregister():
    return register.handleregister(request)


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
        return booking.get_booking(request, id)
    return booking.book(request, id)


@app.route("/calendar")
def routecalendar():
    return service_calendar.get_calendar(request)
