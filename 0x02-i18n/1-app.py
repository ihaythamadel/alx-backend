#!/usr/bin/env python3

"""
1-app.py
Module that starts a Flask web application with Babel integration

Imports:
    flask.Flask to setup the web application
    flask.render_template to render the HTML files
    flask_babel.Babel for internationalization support

Classes:
    Config: Configuration class for Babel

Functions:
    index: Returns the rendered template for the '/' route

App Routing:
    @app.route('/') -> Calls the index function to return the HTML page

Running:
    The application runs on host 0.0.0.0 and port 5000
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Babel
    Attributes:
        LANGUAGES (list): The list of
        languages supported by the web application
        BABEL_DEFAULT_LOCALE (str): The default language locale
        BABEL_DEFAULT_TIMEZONE (str): The default timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    index function
    Returns:
        Rendered template for the '/' route
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    """
    MAIN App
    """
    app.run(host='0.0.0.0', port=5000)
