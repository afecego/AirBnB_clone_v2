#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<s_id>', strict_slashes=False)
def id_list(s_id=None):
    if s_id is not None:
        s_id = 'State.' + s_id
    states = storage.all(State)
    return render_template('9-states.html', city_state=states, id_city=s_id)


@app.teardown_appcontext
def appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
