from flask import Flask
from flask_bootstrap import Bootstrap
from flask_dropzone import Dropzone
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import competition
from competition.assets import assets
from competition.utils import Permission
from .config import config as app_config

# Create extension instances
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
dropzone = Dropzone()

# Import models - this has to be after "db = SQLAlchemy()" line
from competition.models.Role import Role
from competition.models.Competition import Competition
from competition.models.Field import Field
from competition.models.Associations import Ownership
from competition.models.Participation import Participation
from competition.models.Question import Question
from competition.models.Result import Result
from competition.models.User import User
from competition.models.Student import Student
from competition.models.Administrator import Administrator
from competition.models.AnonymousUser import AnonymousUser

# Setup extensions
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.anonymous_user = AnonymousUser


def create_app(config_name="default"):
	""" App Factory Function """
	app = Flask(__name__)
	app.config.from_object(app_config[config_name])
	app_config[config_name].init_app(app)

	register_extensions(app)
	register_blueprints(app)
	register_globals(app)

	return app


def register_extensions(app):
	""" Attach and initialize extensions here """
	with app.app_context():
		db.init_app(app)

	bootstrap.init_app(app)
	assets.init_app(app)
	login_manager.init_app(app)
	dropzone.init_app(app)


def register_blueprints(app):
	""" Attach routes and blueprints here """
	from competition.controllers.public import public_bp
	from competition.controllers.auth import auth_bp
	from competition.controllers.competition import competition_bp
	from competition.controllers.competitors import competitors_bp
	from competition.blueprints.api import api as api_blueprint

	app.register_blueprint(public_bp)
	app.register_blueprint(auth_bp, url_prefix='/auth')
	app.register_blueprint(competition_bp, url_prefix='/competition')
	app.register_blueprint(competitors_bp, url_prefix='/competitors')
	app.register_blueprint(api_blueprint, url_prefix='/api')


def register_globals(app):
	""" Register globally (including templates) available variables and functions. """

	@app.context_processor
	def inject_permission_check():
		from flask_login import AnonymousUserMixin

		def is_admin(usr):
			return type(usr) is not AnonymousUserMixin and usr.is_administrator()

		def is_student(usr):
			return type(usr) is not AnonymousUserMixin and usr.can(Permission.STUDENT_ACCESS)

		return dict(
			permission=Permission,
			is_student=is_student,
			is_admin=is_admin
		)

	@app.context_processor
	def inject_association_check():
		def is_owner(usr, comp):
			return usr.id in [o.id for o in comp.owners]

		return dict(is_owner=is_owner)
