from flask import session, render_template
import db


def get_booking(req, id):
    if "username" in session:
        service = db.get_service(id)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        return render_template("booking.html", product=service, days=days)
    else:
        return render_template("error.html", errmsg="You must be logged in to book services")
