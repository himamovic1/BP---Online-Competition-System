from competition.controllers.public.views import Public
from . import html_blueprint


@html_blueprint.route('/')
def index():
    public = Public()
    return public.index()


@html_blueprint.route('/home')
def home():
    public = Public()
    return public.home()
