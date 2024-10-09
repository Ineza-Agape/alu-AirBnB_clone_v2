#!/usr/bin/python3
"""
Module: web_flask
Description: A Flask web application that serves different routes
    with specific outputs.

This module creates a Flask web application that listens on 0.0.0.0:5000
and provides several routes:
    - /: displays "Hello HBNB!"
    - /hbnb: displays "HBNB"
    - /c/<text>: displays "C " followed by the value of text with
      underscores replaced by spaces
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display text after replacing underscores with spaces.
    
    Args:
        text (str): The input text where underscores will be replaced

    Returns:
        str: A string starting with 'C ' followed by the modified text
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)