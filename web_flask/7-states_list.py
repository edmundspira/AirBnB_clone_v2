#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    store = storage.all("State")
    return render_template('7-states_list.html', storage=store.values)


@app.teardown_appcontext
def teardown(error):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
