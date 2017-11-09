from flask import Blueprint

competition_bp = Blueprint('competition', __name__)

from . import views