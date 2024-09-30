from flask import session, render_template
import db


def get_booking(req, id):
    if "username" not in session:
        return render_template("error.html", errmsg="You must be logged in to book services")
    service = db.get_service(id)
    if not service:
        return render_template("error.html", errmsg="Could not find service")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    times = []
    for day in days:
        time = {}
        time["weekday"] = day
        time["slots"] = [1, 2, 3, 4]
        times.append(time)
    return render_template("booking.html", product=service, times=times)
