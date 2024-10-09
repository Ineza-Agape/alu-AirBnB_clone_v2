#!/usr/bin/python3
"""
This script contains the code for three routes
 1. /
 2. /hbnb
 3. /c/<text> where the text is dynamic
 4. /python/<text> where the text is dynamic, and it will be displayed. 
   if the text is not provided, the default will show up
"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display 'HBNB'."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route to display 'C <text>', where <text> replaces underscores with spaces."""
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route to display 'Python <text>', where <text> replaces underscores with spaces.
    
    If no <text> is provided, defaults to 'is cool'.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

