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

    free_slots = get_weeks_free_slots(monday, service[3])
    return render_template("booking.html", product=service, dayslots=free_slots, week=date.isocalendar()[1])


def get_weeks_free_slots(start_date: datetime.date, duration: datetime.timedelta):
    dayslots = []
    for day in range(7):
        dayslots.append(get_free_slots(start_date + datetime.timedelta(days=day), duration))
    return dayslots


def get_free_slots(date, duration):
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = {}
    day["weekday"] = weekdays[date.weekday()]
    day["slots"] = []
    day["date"] = date
    opening_hours = db.get_hours(date)
    if not opening_hours:
        day["open"] = False
        return day
    day["open"] = True

    taken_times = db.get_bookings(date)
    block_size = datetime.timedelta(minutes=20)
    start = opening_hours[0]
    close = opening_hours[1]
    j = 0

    while start + duration <= close:
        end = start + duration
        if len(taken_times) > 0 and j < len(taken_times):
            if end <= taken_times[j][2]:
                day["slots"].append((start, end))
            else:
                start = taken_times[j][2] + taken_times[j][1]
                j += 1
                continue
        else:
            day["slots"].append((start, end))
        start += block_size
    return day
