from app import app
from db import db
import register
import login
from flask import redirect, render_template, request, session
from sqlalchemy.sql import text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def routelogin():
    return login.handlelogin(request)


@app.route("/logout")
def routelogout():
    del session["username"]
    del session["admin"]
    return redirect(request.referrer)


@app.route("/register", methods=["GET", "POST"])
def routeregister():
    return register.handleregister(request)


@app.route("/error")
def error(err="There was an error"):
    return render_template("error.html", errmsg=err)


@app.route("/products")
def products():
    query = text("SELECT * FROM service_items WHERE active=TRUE")
    result = db.session.execute(query).fetchall()
    return render_template("products.html", products=result)


@app.route("/products/<int:id>/book")
def book(id):
    if "username" in session:
        query = text("SELECT * FROM service_items WHERE service_id=:id")
        result = db.session.execute(query, {"id": id}).fetchone()
        return render_template("booking.html", product=result)
    else:
        return render_template("error.html", errmsg="You must be logged in to book services")
