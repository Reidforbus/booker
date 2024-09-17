from flask import Flask
from flask import redirect, render_template, request, session, url_for
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
import logging

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return redirect("/")
    username = request.form["username"]
    # password = request.form["pwd"]
    # TODO: validate credentials
    query = text("SELECT admin FROM users WHERE username=:username")
    result = db.session.execute(query, {"username": username}).fetchone()
    if result is not None:
        session["username"] = username
        session["admin"] = result.admin
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    del session["admin"]
    return redirect("/")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def handleregister():
    username = request.form["username"]
    if username == "":
        return redirect("/error")
    sameusrnm = text("SELECT COUNT(*) FROM users WHERE username=:username")
    result = db.session.execute(sameusrnm, {"username": username}).fetchone()
    app.logger.debug(result[0])
    if result[0] == 1:
        return redirect("/error")
    name = request.form["name"]
    pwd_hash = generate_password_hash(request.form["pwd"])
    sqlinsert = "INSERT INTO users (username, pwd, name) VALUES (:username, :pwd, :name)"
    db.session.execute(text(sqlinsert), {"username":username, "pwd":pwd_hash, "name":name})
    db.session.commit()
    return redirect("/")


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/products")
def products():
    return render_template("products.html", products=[{"name": "ABC"}, {"name": "XYZ"}])


def is_admin():
    if session["username"]:
        return session["admin"]
    return False
