#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import render_template
from models.state import State
from models.city import City
from models import storage
from flask import Flask
import os

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def citiesbystates():
    """ method to retrieve all the cities of each state """
    dct1 = storage.all(State)
    lt1 = []
    for i in dct1.values():
        lt1.append(i)
    return render_template("8-cities_by_states.html", states=lt1)


@app.teardown_appcontext
def teardown_db(exception):
    """ method to close the session after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
