from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html", motd="Book your time here")


@app.route("/login", methods=["POST"])
def login():
    user = request.form["email"]
    # password = request.form["pwd"]
    # TODO: validate credentials
    session["user"] = user
    return redirect("/")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect("/")
