from flask import render_template, flash
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from competition.controllers.competitors.forms import AddCompetitorForm
from competition.controllers.competitors import competitors_bp
from competition.decorators import admin_required, student_required

from competition.services.participation import ParticipationService
from competition.services.student import StudentService


@competitors_bp.route('/view/all')
@login_required
@admin_required
def list_all():
    data = ParticipationService.read_all()
    return render_template('competitors/list.html', competitor_list=data)


@competitors_bp.route('/add/new', methods=['GET', 'POST'])
@login_required
@admin_required
def add_new():
    form = AddCompetitorForm()

    if form.validate_on_submit():
        comp = ParticipationService.create(form.name.data, form.surname.data, form.index_number.data, form.year.data,
                                           form.competition_date.data, form.competition_name.data)

        if comp is None:
            flash('Nije moguće dodati takmičara.')
        else:
            flash('Takmičar uspješno dodan.')
            return redirect('competitors/view/all')

    return render_template('competitors/add_new.html', form=form)


@competitors_bp.route('/update/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def update(id):
    participation = ParticipationService.read(id=id)
    usr = StudentService.read(user_id=participation.user_id)
    form = AddCompetitorForm()

    form.name.data = usr.name
    form.surname.data = usr.surname
    form.index_number.data = usr.index_number
    form.year.data = usr.study_year

    # if form.validate_on_submit():
    #     ParticipationService.update()
    #     flash("Uspješna izmjena podataka")
    #     return list_all()
    # else:
    #     flash("Pogrešno uneseni podaci")

    return render_template('competitors/add_new.html', form=form)


# @competition_bp.route('/delete/<name>/<date>')
# @login_required
# def delete(name, date):
#     CompetitionService.delete(name, date)
#     flash('Uspješno ste obrisali takmičara')
#     return list_all()

@competitors_bp.route('/stats/fields', methods=['GET'])
@competitors_bp.route('/stats/fields/<for_user>', methods=['GET'])
@login_required
def show_stats_by_field(for_user=None):
    from competition import Competition, Result, Participation, Student, Field
    from competition import db

    from sqlalchemy.sql import label
    from sqlalchemy import func, and_

    if not for_user:
        for_user = current_user.id

    # Participates per field (Should be placed in pie chart)
    ppf = db.session.query(Field.name, label('count', func.count(Participation.id))) \
        .group_by(Field.id) \
        .filter(Field.id == Competition.field_id) \
        .filter(and_(Competition.name == Participation.competition_name, Competition.date == Participation.competition_date)) \
        .filter(Participation.user_id == for_user) \
        .all()

    # Maximum points per field (Should be placed in bar chart)
    mppf = db.session.query(Field.name, label('maximum', func.max(Result.points_scored))) \
        .group_by(Field.id) \
        .filter(Field.id == Competition.field_id) \
        .filter(and_(Competition.name == Participation.competition_name, Competition.date == Participation.competition_date)) \
        .filter(Participation.id == Result.participation_id) \
        .filter(Participation.user_id == for_user) \
        .all()

    # Points scored in competitions grouped by fields
    overall_score = db.session.query(Field.name, Competition.name, label('points', func.max(Result.points_scored))) \
        .group_by(Field.id, Competition.name) \
        .filter(Field.id == Competition.field_id) \
        .filter(and_(Competition.name == Participation.competition_name, Competition.date == Participation.competition_date)) \
        .filter(Participation.id == Result.participation_id) \
        .filter(Participation.user_id == for_user) \
        .all()

    return render_template('competitors/stats.html', ppf=ppf, mppf=mppf, overall_score=overall_score)
