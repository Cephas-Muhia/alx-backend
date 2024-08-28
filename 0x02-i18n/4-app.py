#!/usr/bin/env python3
"""A simple flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)

