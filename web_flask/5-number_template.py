#!/usr/bin/python3
"""
Start my framework application
"""
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Message to index application"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def CText(text):
    """Using my variable to at url text"""
    textC = text.replace('_', ' ')
    return ("C {}".format(escape(textC)))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text):
    """
    Two routes, the firts is for home python,
    the next route is for the arguments inserted for the user
    """
    txt = text.replace('_', ' ')
    return "Python {}".format(escape(txt))


@app.route('/number/<int:n>', strict_slashes=False)
def numberText(n):
    """This funtion is for know if the a number is integer"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def numText(n):
    """This funtion show the number in the page, if is a number integer"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
