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
def hello():
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        dct1 = storage.all(State)
        lt1 = []
        for i in dct1.values():
            lt1.append(i)
    else:
        dct1 = storage.all(State)
        lt1 = []
        for i in dct1.values():
            lt1.append(str(i.cities))
    return (str(lt1[0].cities))

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)