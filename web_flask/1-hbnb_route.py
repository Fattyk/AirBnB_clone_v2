#!/usr/bin/python3
"""This module defines a flask function
that displays 'Hello HBNB!' and 'HBNB'
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


if __name__ == "__main__":
    """Entry point"""
    app.run(host='0.0.0.0', port=5000)
