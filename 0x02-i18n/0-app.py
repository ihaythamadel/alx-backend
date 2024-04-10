#!/usr/bin/env python3

"""
0-app.py
Module that starts a Flask web application

Imports:
    flask.Flask to setup the web application
    flask.render_template to render the HTML files

Functions:
    index: Returns the rendered template for the '/' route

App Routing:
    @app.route('/') -> Calls the index function to return the HTML page

Running:
    The application runs on host 0.0.0.0 and port 5000
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    index function
    Returns:
        Rendered template for the '/' route
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    """
    MAIN App
    """
    app.run(host='0.0.0.0', port=5000)
