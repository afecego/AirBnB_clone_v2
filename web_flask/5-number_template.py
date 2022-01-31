#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def hello_addtext(text):
    add = text.replace("_", " ")
    return 'C {}'.format(add)


@app.route('/python')
@app.route('/python/<text>')
def hello_phytontext(text='is cool'):
    add = text.replace("_", " ")
    return 'Python {}'.format(add)


@app.route('/number/<int:n>')
def hello_numbre(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def hello_template(n=None):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
