from flask import jsonify
from datetime import datetime

from competition.controllers.public.views import Public
from . import api as api_blueprint


# API test endpoints
@api_blueprint.route('/<int:number>')
def api_test(number):
    response = jsonify({'input': number, 'result': number * 20})
    response.status_code = 200
    return response


@api_blueprint.route('/create_field/<name>')
def create_field(name):
    pub = Public()
    pub.create_field(name)

    response = jsonify({'status': 'shall be added'})
    response.status_code = 200
    return response
