# Code taken from "The New and Improved Flask Mega-Tutorial (2024 Edition)" by Miguel Grinberg
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
