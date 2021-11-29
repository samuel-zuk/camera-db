import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from camera_db.common.conf import get_config
from camera_db.utils.db import db_uri_from_config


def setup_app(devel=False):
    app = Flask(__name__)
    app.config.update(get_config())
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri_from_config(app.config)
    # NOTE: This silences a warning from Flask-SQLAlchemy. Decision was made
    # based on info from this StackOverflow thread:
    # https://stackoverflow.com/questions/33738467
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    if not devel:
        return app.wsgi_app
    else:
        app.run(host='0.0.0.0', port=5000, debug=True)
        sys.exit()


class CameraDBApp(object):
    def __init__(self):
        self.app = setup_app()

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)
