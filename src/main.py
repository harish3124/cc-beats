from flask import Flask, render_template
import flask.json as json
from random import randrange
from . import scraper

app = Flask(__name__)
library = scraper.init()


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/banner")
def banner():
    (url, attr_text) = get_rand()
    return render_template("obs-card.html", url=url, attr_text=attr_text)


@app.route("/random")
def random_track():
    (url, attr_text) = get_rand()
    return json.jsonify(f"src: {url}; attributionText: {attr_text}")


def get_rand():
    rand = randrange(len(library))
    return library[rand]
