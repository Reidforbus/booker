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
    print("Free slots:", free_slots)
    return render_template("booking.html", product=service, dayslots=sampletimes(), week=date.isocalendar()[1])


def sampletimes():
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    times = []
    for day in weekdays:
        time = {}
        time["weekday"] = day
        time["slots"] = [1, 2, 3, 4]
        times.append(time)
    return times


def get_free_slots(start_date: datetime.date, duration: datetime.timedelta):
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    dayslots = []
    for offset in range(7):
        day = {}
        date = start_date + datetime.timedelta(days=offset)
        day["weekday"] = weekdays[date.weekday()]
        day["slots"] = []
        opening_hours = db.get_hours(date)
        if not opening_hours:
            dayslots.append(day)
            continue
        taken_times = db.get_bookings(date)
        print("Day:", offset, opening_hours, taken_times)

        block_size = datetime.timedelta(minutes=20)
        start = datetime.datetime.combine(date, opening_hours[0])
        close = datetime.datetime.combine(date, opening_hours[1])
        j = 0

        while start + duration <= close:
            end = start + duration
            if len(taken_times) > 0 and j < len(taken_times):
                if end.time() <= taken_times[j][2]:
                    day["slots"].append((start.time(), end.time()))
                else:
                    start = datetime.datetime.combine(date, taken_times[j][2]) + taken_times[j][1]
                    j += 1
                    continue
            else:
                day["slots"].append((start.time(), end.time()))
            start += block_size
        dayslots.append(day)
    return dayslots
