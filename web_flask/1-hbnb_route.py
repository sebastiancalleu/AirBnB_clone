#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ method to retrieve a string """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ method to retrieve a string """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
