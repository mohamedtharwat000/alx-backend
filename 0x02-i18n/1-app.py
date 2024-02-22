#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from babel import Babel

app = Flask(__name__)
bable = Babel(app)


class Config:
    """ Babel Configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    """GET /
    """
    return render_template('1-index.html')
