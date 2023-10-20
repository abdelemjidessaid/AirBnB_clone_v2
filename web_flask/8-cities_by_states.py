#!/usr/bin/python3
"""
    this module contains a script that starts Flask app
    and loads all cities and states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states')
def get_cities_by_states():
    """
        get_cities_by_states function that renders an HTML file contains
        all states and ites cities ordered.
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.py', states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
        app_teardown function that cleans up the app, and closes the
        session of SQLAlchemy.
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
