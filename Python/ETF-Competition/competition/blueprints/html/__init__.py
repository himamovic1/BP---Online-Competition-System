from flask import Blueprint

html_blueprint = Blueprint('html', __name__)

from . import pages, errors
