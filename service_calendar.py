from flask import render_template, session
import datetime
import db

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def get_calendar(req):
    if "admin" not in session or not session["admin"]:
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
        day["slots"] = []
        for booking in bookings:
            end = datetime.datetime.combine(date, booking.time) + booking.dur
            day["slots"].append((booking, end.time()))
        day["date"] = querydate
        days.append(day)

    return render_template("calendar.html", days=days, week=date.isocalendar()[1], nav=nav)
