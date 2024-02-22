#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel, dates
from datetime import datetime
import pytz
from zoneinfo import ZoneInfo

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Babel Configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    if "locale" in request.args.keys():
        return request.args["locale"]
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request():
    """before requests"""
    g.user = get_user()


def get_user():
    """get user data by user's id"""
    id = request.args.get("login_as")
    if id is None or int(id) not in users.keys():
        return None
    return users[int(id)]


@babel.timezoneselector
def get_timezone():
    """define the timezone"""
    try:
        if "timezone" in request.args.keys():
            pytz.timezone(request.args["timezone"])
            return request.args["timezone"]
        if g.user and "timezone" in g.user.keys():
            pytz.timezone(g.user["timezone"])
            return g.user["timezone"]
        return app.config["BABEL_DEFAULT_TIMEZONE"]
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/", methods=["GET"])
def index() -> str:
    """GET /"""
    date = datetime.now(tz=ZoneInfo(get_timezone()))
    formatted_datetime = dates.format_datetime(date, locale=get_locale())
    return render_template("index.html", user=g.user, date=formatted_datetime)


if __name__ == "__main__":
    app.run(debug=True)
