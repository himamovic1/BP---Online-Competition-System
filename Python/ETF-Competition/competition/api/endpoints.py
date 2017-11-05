from competition.controllers.public.views import Public
from . import api as api_scheme


# HTML Test endpoints
@api_scheme.route('/')
def index():
    public = Public()
    return public.index()


@api_scheme.route('/home')
def home():
    public = Public()
    return public.home()


# API test endpoints
@api_scheme.route('/api/<int:number>')
def api_test(number):
    data = {'input': number, 'result': number * 20}
    return data.__str__(), 200
