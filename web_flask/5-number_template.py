#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello():
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

@app.route("/c/<text>")
def cisfun(text=None):
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python")
@app.route("/python/<text>")
def pythonistheway(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:text>")
def isnumber(text):
    return "{} is a number".format(text)

@app.route("/number_template/<int:text>")
def isnumberhtml(text):
    return render_template('5-number.html', n=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)