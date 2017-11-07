from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config as app_config

# Create extension instances
db = SQLAlchemy()

# Import models - this has to be after "db = SQLAlchemy()" line
from competition.models.Competition import Competition
from competition.models.Field import Field
from competition.models.Ownership import Ownership
from competition.models.Participation import Participation
from competition.models.Question import Question
from competition.models.Result import Result
from competition.models.User import User
from competition.models.Student import Student
from competition.models.Administrator import Administrator


def create_app(config_name="default"):
    """ App Factory Function """
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """ Attach and initialize extensions here """
    with app.app_context():
        db.init_app(app)


def register_blueprints(app):
    """ Attach routes and blueprints here """
    from competition.blueprints.api import api as api_scheme_v1
    from competition.blueprints.html import html_blueprint as browser_scheme

    app.register_blueprint(api_scheme_v1, url_prefix='/api')
    app.register_blueprint(browser_scheme)
