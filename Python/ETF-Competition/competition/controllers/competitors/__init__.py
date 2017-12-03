from flask import Blueprint

competitors_bp = Blueprint('competitors', __name__)

from . import views