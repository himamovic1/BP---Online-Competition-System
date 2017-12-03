from flask import render_template, flash
from flask_login import login_required
from werkzeug.utils import redirect

from competition.controllers.competitors.forms import AddCompetitorForm
from competition.controllers.competitors import competitors_bp

from competition.services.participation import ParticipationService
from competition.services.student import StudentService


@competitors_bp.route('/view/all')
@login_required
def list_all():
    data = ParticipationService.read_all()
    return render_template('competitors/list.html', competitor_list=data)


@competitors_bp.route('/add/new', methods=['GET', 'POST'])
@login_required
def add_new():
    form = AddCompetitorForm()

    if form.validate_on_submit():
        comp = ParticipationService.create(form.name.data, form.surname.data, form.index_number.data, form.year.data, form.competition_date.data, form.competition_name.data)

        if comp is None:
            flash('Nije moguće dodati takmičara.')
        else:
            flash('Takmičar uspješno dodan.')
            return redirect('competitors/view/all')

    return render_template('competitors/add_new.html', form=form)


@competitors_bp.route('/update/<id>', methods=['GET', 'POST'])
@login_required
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
