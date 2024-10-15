from app import app
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash
import datetime

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


def get_user(username):
    query = text("SELECT * FROM users WHERE username=:username")
    return db.session.execute(query, {"username": username}).fetchone()


def user_exists(username):
    query = text("SELECT COUNT(*) FROM users WHERE username=:username")
    return 1 == db.session.execute(query, {"username": username}).fetchone()[0]


def add_user(username, pwd, name, admin):
    insertquery = "INSERT INTO users (username, pwd, name, admin) VALUES (:username, :pwd, :name, :admin)"
    pwd_hash = generate_password_hash(pwd)
    db.session.execute(text(insertquery), {"username": username, "pwd": pwd_hash, "name": name, "admin": admin})
    db.session.commit()


def get_service(id):
    query = text("SELECT * FROM service_items WHERE service_id=:id")
    return db.session.execute(query, {"id": id}).fetchone()


def get_services():
    query = text("SELECT * FROM service_items WHERE active=TRUE")
    return db.session.execute(query).fetchall()


def get_bookings(date):
    query = text(
            "SELECT b.service_id, dur, time"
            + " FROM bookings AS b"
            + " JOIN service_items AS s ON b.service_id = s.service_id"
            + " WHERE day=:date"
            + " ORDER BY time"
            )
    result = db.session.execute(query, {"date": date}).fetchall()
    bookings = []
    for booking in result:
        bookings.append((booking[0], booking[1], datetime.datetime.combine(date, booking[2])))
    return bookings


def get_detailed_bookings(date):
    query = text(
            "SELECT s.name AS service, time, dur, u.name"
            + " FROM bookings AS b"
            + " JOIN service_items AS s ON b.service_id = s.service_id"
            + " JOIN booking_info AS i ON b.booking_id = i.booking_id"
            + " JOIN users AS u ON i.user_id = u.user_id"
            + " WHERE day = :date"
            + " ORDER BY time"
            )
    result = db.session.execute(query, {"date": date}).fetchall()
    return result


def get_hours(date):
    query = text("SELECT open, close FROM open_hours WHERE day=:date")
    result = db.session.execute(query, {"date": date}).fetchone()
    if not result:
        return None
    open = datetime.datetime.combine(date, result[0])
    close = datetime.datetime.combine(date, result[1])
    return (open, close)


def make_booking(id: int, start: datetime.datetime, msg, user):
    bookingquery = text("INSERT INTO bookings (booking_id, service_id, time, day) VALUES (:booking_id, :service_id, :time, :day)")
    infoquery = text("INSERT INTO booking_info (msg, user_id) VALUES (:msg, :user_id) RETURNING booking_id")
    booking_id = db.session.execute(infoquery, {"msg": msg, "user_id": user}).fetchone()[0]
    db.session.execute(bookingquery, {"booking_id": booking_id, "service_id": id, "time": start.time(), "day": start.date()})
    db.session.commit()


def get_users():
    query = text("SELECT name, username, admin FROM users")
    return db.session.execute(query).fetchall()


def edit_service(id, details):
    updatequery = text(
            "UPDATE service_items"
            + " SET (name, description, price, dur)"
            + " = (:name, :desc, :price, :dur)"
            + " WHERE service_id = :id"
            )
    result = db.session.execute(updatequery,
                                {"name": details["name"],
                                 "desc": details["desc"],
                                 "price": details["price"],
                                 "dur": details["dur"] + "minutes",
                                 "id": id})
    if result.rowcount == 1:
        db.session.commit()
        return True
    else:
        db.session.rollback()
        return False


def add_service(details):
    insertquery = text(
            "INSERT INTO service_items"
            + " (name, description, price, dur)"
            + " VALUES (:name, :desc, :price, :dur)"
            + " RETURNING service_id"
            )
    result = db.session.execute(insertquery,
                                {"name": details["name"],
                                 "desc": details["desc"],
                                 "price": details["price"],
                                 "dur": details["dur"] + "minutes",
                                 "id": id}).fetchone()
    if result is not None:
        db.session.commit()
        return result[0]
    else:
        db.session.rollback()
        return None
