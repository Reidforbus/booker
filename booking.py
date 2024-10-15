from flask import session, render_template
import db
import datetime
from logic import csrf_valid

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


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
    nav = {}
    nav["lastweek"] = (monday - datetime.timedelta(weeks=1)).isoformat()
    nav["nextweek"] = (monday + datetime.timedelta(weeks=1)).isoformat()
    return render_template("booking.html", service=service, dayslots=free_slots, week=date.isocalendar()[1], nav=nav)


def get_weeks_free_slots(start_date: datetime.date, duration: datetime.timedelta):
    dayslots = []
    for day in range(7):
        dayslots.append(get_free_slots(start_date + datetime.timedelta(days=day), duration))
    return dayslots


def get_free_slots(date, duration):
    day = {}
    day["weekday"] = weekdays[date.weekday()]
    day["slots"] = []
    day["date"] = date
    opening_hours = db.get_hours(date)
    if not opening_hours or date <= datetime.date.today():
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


def book(req, id):
    if csrf_valid(req):
        return render_template("error.html", errmsg="Invalid request")
    slot = req.form.get("slot")
    start, end = slot.split(";")
    start = datetime.datetime.fromisoformat(start)
    end = datetime.datetime.fromisoformat(end)
    if not valid_booking(start, end):
        return render_template("error.html", errmsg=f"{start} --- {end} is not available for booking!")
    service = db.get_service(id)
    if not service:
        return render_template("error.html", errmsg=f"Service id {id} does not exist")
    stage = req.form.get("stage")
    if stage == "0":
        return render_template("fillbooking.html", service=service, slot=slot)
    elif stage == "1":
        msg = req.form.get("msg")
        return render_template("confirmbooking.html", service=service, slot=slot, msg=msg)
    elif stage == "2":
        msg = req.form.get("msg")
        db.make_booking(id, start, msg, session["user_id"])
        return render_template("error.html", errmsg="Booking made succesfully")
    return render_template("error.html", errmsg="Something went wrong here")


def valid_booking(start, end):
    hours = db.get_hours(start.date())
    if not hours:
        return False
    print("hours ok")
    open, close = hours
    if open > start or close < end:
        return False
    print("between open hours ok")
    taken = db.get_bookings(start.date())
    for (_, dur, time) in taken:
        if not (end <= time or start >= time + dur):
            print(f"Failed on {time} - {dur}")
            return False
    print("fits with other bookings ok")
    return True
