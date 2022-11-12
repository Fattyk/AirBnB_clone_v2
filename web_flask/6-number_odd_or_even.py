#!/usr/bin/python3
"""This module define and starts a flask function
/number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This root function return Hello HBNB to user"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function reurns HBNB when /hbnb is routed"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display C plus the given text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """Display python plus the given text or default text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    if (n%2 == 0):
        return render_template("6-number_odd_or_even.html", even=n)
    return render_template("6-number_odd_or_even.html", odd=n)


if __name__ == "__main__":
    """Entry point"""
    app.run(host='0.0.0.0', port=5000)
