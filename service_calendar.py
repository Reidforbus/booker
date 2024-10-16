from flask import render_template, redirect
from logic import is_admin, csrf_invalid
import datetime
import db

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def get_calendar(req):
    if not is_admin():
        return render_template("error.html", errmsg="You don't have permission to do that")
    date = req.args.get("date")
    if not date:
        date = datetime.date.today()
    else:
        try:
            date = datetime.date.fromisoformat(date)
        except ValueError:
            return render_template("error.html", errmsg="Date was not valid")

    monday = date - datetime.timedelta(days=date.weekday())
    nav = {}
    nav["lastweek"] = (monday - datetime.timedelta(weeks=1)).isoformat()
    nav["nextweek"] = (monday + datetime.timedelta(weeks=1)).isoformat()
    days = []

    for weekday in range(7):
        day = {}
        querydate = monday + datetime.timedelta(days=weekday)
        day["weekday"] = "Today" if querydate == datetime.date.today() else weekdays[weekday]
        bookings = db.get_detailed_bookings(querydate)
        open_hours = db.get_hours(querydate)
        if not open_hours:
            day["open"] = None
            day["close"] = None
        else:
            day["open"] = open_hours[0]
            day["close"] = open_hours[1]
        day["past"] = querydate <= datetime.date.today()
        day["slots"] = []
        for booking in bookings:
            end = datetime.datetime.combine(date, booking.time) + booking.dur
            day["slots"].append((booking, end.time()))
        day["date"] = querydate
        days.append(day)

    return render_template("calendar.html", days=days, week=date.isocalendar()[1], nav=nav)


def set_hours(req):
    if not is_admin():
        return render_template("error.html", errmsg="You don't have permission to do that")
    if req.method == "GET":
        date = req.args.get("date")
        if not date:
            date = datetime.date.today()
        else:
            try:
                date = datetime.date.fromisoformat(date)
            except ValueError:
                return render_template("error.html", errmsg="Date was not valid")
        return render_template("hours.html", date=date)
    if req.method == "POST":
        if csrf_invalid(req):
            return render_template("error.html", errmsg="Invalid request")
        try:
            date = datetime.date.fromisoformat(req.form.get("date"))
            open = datetime.time.fromisoformat(req.form.get("open_time"))
            close = datetime.time.fromisoformat(req.form.get("close_time"))
        except ValueError:
            return render_template("error.html", errmsg="At least one value was invalid")
        if db.set_hours(date, open, close):
            return redirect(f"/calendar?date={ date.isoformat() }")
        return render_template("error.html", errmsg="Could not update hours")
