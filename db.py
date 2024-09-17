from app import app
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


def validate_login(username, pwd):
    # TODO validate login with password
    query = text("SELECT admin FROM users WHERE username=:username")
    return db.session.execute(query, {"username": username}).fetchone()
