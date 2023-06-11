from flask import Flask
from random import randrange
from . import scraper

app = Flask(__name__)
library = scraper.init()

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/api")
def api():
    return str(get_random_track())

def get_random_track():
    rand = randrange(len(library))
    return library[rand]
