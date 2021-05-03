#!/usr/bin/python3
"""
    A simple flask exemple with 3 routes
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Says Hello on the home page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to HBNB page"""
    return 'HBNB'


@app.route('/c/<path>', strict_slashes=False)
def c_is(path):
    """Route to /c/catch_all"""
    return 'C {}'.format(path.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
