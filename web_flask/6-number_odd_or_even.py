#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def start_app():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def text(text):
    """display “C ” followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def pyiscool(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    if (text == 'is cool'):
        return 'Python {}'.format(text)
    else:
        return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def template(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        outcome = 'even'
    else:
        outcome = 'odd'
    return render_template('6-number_odd_or_even.html', num=n,
                           outcome=outcome)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
