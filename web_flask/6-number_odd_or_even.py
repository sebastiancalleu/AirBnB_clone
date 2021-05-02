#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template

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


@app.route("/number_template/<int:text>")
def isnumberhtml(text):
    """ method to render a html with a number pass as an arguments """
    return render_template('5-number.html', n=text)


@app.route("/number_odd_or_even/<int:text>")
def oddoreven(text):
    """ method to render a html with a number and a text """
    if text % 2 == 0:
        kind = "even"
    else:
        kind = "odd"
    return render_template('6-number_odd_or_even.html', n=text, kind=kind)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
