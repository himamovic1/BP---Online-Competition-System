import datetime

from flask import jsonify, request

from competition import User
from competition.services.student import StudentService
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


@api_blueprint.route('/search/student')
def search_students():
    name = request.args.get('name')
    surname = request.args.get('surname')
    index = request.args.get('index')
    study_year = request.args.get('year')

    students = StudentService.search_by_attributes(name=name, surname=surname, index=index, study_year=study_year)
    response = {}
    response_len = len(students)

    for i in range(response_len):
        response[i] = students[i].as_dict()
        response[i]["name"] = students[i].name
        response[i]["surname"] = students[i].surname

    response = jsonify(response)
    response.status_code = 200

    return response