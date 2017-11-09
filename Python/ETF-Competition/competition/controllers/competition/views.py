from flask import render_template
from flask_login import login_required

from competition.controllers.competition import competition_bp


@competition_bp.route('/view/all')
@login_required
def competition_list():
    return render_template('competition/competition_list.html')
