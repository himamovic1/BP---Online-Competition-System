from flask import render_template
from flask_login import login_required

from competition.controllers.competition import competition_bp


@competition_bp.route('/view/all')
@login_required
def list_all():
    return render_template('competition/list.html')


@competition_bp.route('/view/calendar')
@login_required
def calendar():
    return render_template('competition/calendar.html')


@competition_bp.route('/add/new')
@login_required
def add_new():
    return render_template('competition/add_new.html')



