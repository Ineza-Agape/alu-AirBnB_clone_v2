#!/usr/bin/python3
"""
Module: app
A Flask web application that handles different routes and displays
specific messages based on the URL patterns.

This web application listens on 0.0.0.0:5000 and provides multiple
routes that return different text responses. It includes basic URL
variable handling and string manipulation.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' for the root route.

    Returns:
        str: The string 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' for the /hbnb route.

    Returns:
        str: The string 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C' followed by the value of text variable.

    Args:
        text (str): The text to display after 'C'
                   (underscores are replaced with spaces)

    Returns:
        str: A string starting with 'C' followed by the modified text
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
