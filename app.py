from flask import Flask
from os import getenv
import logging


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
logging.basicConfig(level=logging.DEBUG)
import routes
