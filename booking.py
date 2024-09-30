from flask import session, render_template
import db
import datetime


def get_booking(req, id):
    if "username" not in session:
        return render_template("error.html", errmsg="You must be logged in to book services")

    service = db.get_service(id)
    if not service:
        return render_template("error.html", errmsg="Could not find service")

    date = req.args.get("date")
    if not date:
        date = datetime.date.today()
    else:
        try:
            date = datetime.date.fromisoformat(date)
        except ValueError:
            return render_template("error.html", errmsg="Date is not valid")
    monday = date - datetime.timedelta(days=date.weekday())

    free_slots = get_free_slots(monday, service[3])
    return render_template("booking.html", product=service, dayslots=sampletimes(), week=date.isocalendar()[1])


def sampletimes():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    times = []
    for day in days:
        time = {}
        time["weekday"] = day
        time["slots"] = [1, 2, 3, 4]
        times.append(time)
    return times


def get_free_slots(start_date, duration):
    print(start_date, duration)
