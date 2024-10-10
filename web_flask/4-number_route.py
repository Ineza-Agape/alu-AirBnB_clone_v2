#!/usr/bin/python3
"""
Flask web application script that handles various routes
and displays specific messages based on the URL patterns.
"""
from flask import Flask, abort

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
def c_route(text):
    """
    Route that displays 'C' followed by the value of text
    Args:
        text (str): text to display after 'C'
    Returns:
        str: formatted string with underscores replaced by spaces
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Route that displays 'Python' followed by the value of text
    Args:
        text (str): text to display after 'Python' (defaults to 'is cool')
    Returns:
        str: formatted string with underscores replaced by spaces
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """
    Route that displays 'n is a number' only if n is an integer
    Args:
        n: value to check if it's an integer
    Returns:
        str: message confirming n is a number
    Raises:
        404: if n is not an integer
    """
    try:
        n = int(n)
        return '{} is a number'.format(n)
    except ValueError:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return 'Not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
