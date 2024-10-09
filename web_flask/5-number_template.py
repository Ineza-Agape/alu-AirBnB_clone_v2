#!/usr/bin/python3
"""
Flask web application script that handles various routes
and displays specific messages based on the URL patterns.
The 6th route, /number_template/<int:n> will render an html page
"""
from flask import Flask, render_template
from flask import abort

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
    """Route to display 'C <text>', replacing underscores with spaces."""
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route to display 'Python <text>', with default 'is cool'."""
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route to display '<n> is a number' if n is an integer."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route to display an HTML page with 'Number: n' if n is an integer."""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
