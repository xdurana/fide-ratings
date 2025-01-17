import os

from flask import Flask
from apiv1 import blueprint as apiv1

from models import ratings

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(apiv1)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    RATINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/players.txt')
    app.players = ratings.load_ratings(RATINGS_FILE)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
