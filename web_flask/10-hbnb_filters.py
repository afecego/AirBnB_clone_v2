#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models.state import *
from models.amenity import *
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def id_list():
    amini = storage.all(Amenity)
    state = storage.all(State)
    return render_template('10-hbnb_filters.html', state=state, amenity=amini)


@app.teardown_appcontext
def appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
