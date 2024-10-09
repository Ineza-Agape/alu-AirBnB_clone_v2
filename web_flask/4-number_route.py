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


from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f"C {text}"

#  there will be a default text for this route
@app.route("/python/",defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace("_"," ")
    return f"Python {text}"

# capture the parameter and checks it whether is an integer or not
@app.route('/n/<n>', strict_slashes=False)
def n_number(n):
    if(n.isnumeric()):
        return f"{n} is anumber"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
