from flask import jsonify

from . import api as api_scheme


# API test endpoints
@api_scheme.route('/<int:number>')
def api_test(number):
    response = jsonify({'input': number, 'result': number * 20})
    response.status_code = 200
    return response
