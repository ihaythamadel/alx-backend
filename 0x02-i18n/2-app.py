#!/usr/bin/env python3

"""
2-app.py
Module that starts a Flask web application with Babel
integration and locale selection

Imports:
    flask.Flask to setup the web application
    flask.render_template to render the HTML files
    flask.request to access request data
    flask_babel.Babel for internationalization support

Classes:
    Config: Configuration class for Babel

Functions:
    get_locale: Determines the best language match from client's
    Accept Languages header
    index: Returns the rendered template for the '/' route

App Routing:
    @app.route('/') -> Calls the index function to return the HTML page

Running:
    The application runs on host 0.0.0.0 and port 5000
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Babel
    Attributes:
        LANGUAGES (list): The list of languages supported
        by the web application
        BABEL_DEFAULT_LOCALE (str): The default language locale
        BABEL_DEFAULT_TIMEZONE (str): The default timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    get_locale function
    Returns:
        The best language match from client's Accept
        Languages header
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    index function
    Returns:
        Rendered template for the '/' route
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    """
    MAIN App
    """
    app.run(host='0.0.0.0', port=5000)
