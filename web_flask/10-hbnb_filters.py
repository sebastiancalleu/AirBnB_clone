""" script that starts a Flask web application """

from models.amenity import Amenity
from flask import render_template
from models.state import State
from models.city import City
from models import storage
from flask import Flask
import os

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def statesandamenities(text=None):
    """ method to retrieve all the states and amenities """
    dct1 = storage.all(State)
    lt1 = []
    for i in dct1.values():
        lt1.append(i)
    dct2 = storage.all(Amenity)
    lt2 = []
    for i in dct2.values():
        lt2.append(i)
    return render_template("10-hbnb_filters.html", states=lt1, amenities=lt2)


@app.teardown_appcontext
def teardown_db(exception):
    """ method to close the session after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
