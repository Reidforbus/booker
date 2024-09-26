from app import app
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


def get_user(username):
    query = text("SELECT * FROM users WHERE username=:username")
    return db.session.execute(query, {"username": username}).fetchone()


def user_exists(username):
    query = text("SELECT COUNT(*) FROM users WHERE username=:username")
    return 1 == db.session.execute(query, {"username": username}).fetchone()[0]


def add_user(username, pwd, name):
    insertquery = "INSERT INTO users (username, pwd, name) VALUES (:username, :pwd, :name)"
    pwd_hash = generate_password_hash(pwd)
    db.session.execute(text(insertquery), {"username":username, "pwd":pwd_hash, "name":name})
    db.session.commit()
