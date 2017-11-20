import datetime

from flask import jsonify

from . import api as api_blueprint
from competition.services.competition import CompetitionService

# API test endpoints
@api_blueprint.route('/<int:number>')
def api_test(number):
    response = jsonify({'input': number, 'result': number * 20})
    response.status_code = 200
    return response

@api_blueprint.route('/search/competition/<string:search_query>')
def search_competition(search_query):
    competitions = CompetitionService.search(search_query)

    response = {}
    response_len = len(competitions)

    for i in range(response_len):
        field = competitions[i].field.name
        d = competitions[i].date

        response[i] = competitions[i].as_dict()

        response[i]["field"] = field
        response[i]["date"] = d.strftime("%Y-%m-%d %H:%M:%S")

    response = jsonify(response)
    response.status_code = 200

    return response