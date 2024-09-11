from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index(motd="Book your time here"):
    return render_template("index.html", motd=motd)


@app.route("/login", methods=["GET"])
def login():
    return redirect("/")


@app.route("/login", methods=["POST"])
def handlelogin():
    username = request.form["username"]
    # password = request.form["pwd"]
    # TODO: validate credentials
    session["username"] = username
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def handleregister():
    name = request.form["name"]
    username = request.form["username"]
    pwd_hash = generate_password_hash(request.form["pwd"])
    sql = "INSERT INTO users (username, pwd, name) VALUES (:username, :pwd, :name)"
    db.session.execute(text(sql), {"username":username, "pwd":pwd_hash, "name":name})
    db.session.commit()
    return redirect("/")
