#!/usr/bin/python3
"""This module define and starts a flask function
that displays 'Hello HBNB!', 'HBNB' and optional text
"""
from flask import Flask

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
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    """Entry point"""
    app.run(host='0.0.0.0', port=5000)
