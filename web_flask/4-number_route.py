#!/usr/bin/python3
"""
This script contains the code for three routes
 1. /
 2. /hbnb
 3. /c/<text> where the text is dynamic
 4. /python/<text> where the text is dynamic, and it will be displayed. 
   if the text is not provided, the default will show up
 5. /number/<n>
"""


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


# capture the parameter and checks it whether is an integer or not
@app.route('/n/<n>', strict_slashes=False)
def n_number(n):
     # Replace underscores with spaces
    n = n.replace("_"," ")

    # check if it is the number
    if(n.isnumeric()):
        return f"{n} is anumber"


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return 'Not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


