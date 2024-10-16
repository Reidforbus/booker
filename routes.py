from app import app
from login import handlelogin, handlelogout
from register import handleregister
from booking import get_booking, book, view_booking
from users import get_users
from service_calendar import get_calendar, set_hours
from services import get_service, get_services, edit_service, add_service
from flask import render_template, request


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/", methods=["POST", "GET"])
def routelogin():
    return handlelogin(request)


@app.route("/logout/")
def routelogout():
    return handlelogout()


@app.route("/register/", methods=["GET", "POST"])
def routeregister():
    return handleregister(request)


@app.route("/error/")
def error(err="There was an error"):
    return render_template("error.html", errmsg=err)


@app.route("/services/")
def routeservices():
    return get_services(request)


@app.route("/services/<int:id>/")
def routeservice(id):
    return get_service(id, request)


@app.route("/services/<int:id>/book/", methods=["GET", "POST"])
def routebooking(id):
    if request.method == "GET":
        return get_booking(request, id)
    return book(request, id)


@app.route("/calendar/")
def routecalendar():
    return get_calendar(request)


@app.route("/calendar/hours", methods=["GET", "POST"])
def routehours():
    return set_hours(request)


@app.route("/users/")
def routeusers():
    return get_users(request)


@app.route("/services/<int:id>/edit/", methods=["GET", "POST"])
def routeservicesedit(id):
    return edit_service(id, request)


@app.route("/services/add/", methods=["GET", "POST"])
def routeserviceadd():
    return add_service(request)


@app.route("/bookings/<int:id>/", methods=["GET"])
def routeviewbooking(id):
    return view_booking(id, request)
