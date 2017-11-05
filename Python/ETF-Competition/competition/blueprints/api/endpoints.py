from flask import jsonify

from competition.controllers.public.views import Public
from . import api as api_blueprint


# API test endpoints
@api_blueprint.route('/<int:number>')
def api_test(number):
    response = jsonify({'input': number, 'result': number * 20})
    response.status_code = 200
    return response


@api_blueprint.route('/<name>')
def add_new(name):
    pub = Public()
    pub.addNew(name)

    response = jsonify({'status': 'shall be added'})
    response.status_code = 200
    return response