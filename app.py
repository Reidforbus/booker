from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")


@app.route("/")
def index():
    return render_template("index.html", motd="Book your time here")


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
    pwd = request.form["pwd"]
    session["username"] = username
    return redirect("/")
