from flask import render_template

from competition import db
from competition.controllers.public import public_bp
from competition.models.Field import Field


@public_bp.route('/')
def index():
    return render_template('public/index.html')


@public_bp.route('/add/<string:name>')
def create_field(name):
    new_field = Field(name)

    db.session.add(new_field)
    db.session.commit()
