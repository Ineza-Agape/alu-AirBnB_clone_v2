#!/usr/bin/python3
"""
script starts Flask web app
listen on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    """Comment"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template(
        "9-states.html",
        states=states,
        condition="states_list")


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Comment"""
    try:
        state = storage.get(State, id)
        if state is None:
            return render_template("9-states.html", condition="not_found")
        return render_template(
            '9-states.html',
            state=state,
            condition="state_id")
    except:
        return render_template('9-states.html', condition="not_found")


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
