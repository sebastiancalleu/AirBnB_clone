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


@app.route("/c/<text>")
def cisfun(text=None):
    """ method to retrieve a string with arguments"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/<text>")
def pythonistheway(text="is cool"):
    """ method to retrieve a string with arguments"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:text>")
def isnumber(text):
    """ method to retrieve a number pass as an argument. """
    return "{} is a number".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
