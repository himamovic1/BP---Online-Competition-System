from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config as app_config

# Create extension instances
# db = SQLAlchemy()


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
    # db.init_app(app)


def register_blueprints(app):
    """ Attach routes and blueprints here """
    from .api import api as api_scheme_v1

    app.register_blueprint(api_scheme_v1)
