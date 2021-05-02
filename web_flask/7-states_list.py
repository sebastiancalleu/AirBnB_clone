#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import render_template
from models.state import State
from models import storage
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def statesdef():
    """ method to retrieve all states in a database """
    dct1 = storage.all(State)
    lt1 = []
    for i in dct1.values():
        lt1.append(i)
    return render_template("7-states_list.html", states=lt1)


@app.teardown_appcontext
def teardown_db(exception):
    """ method to close the session after each request """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
