from flask import render_template, flash
from flask_login import login_required

from competition.controllers.competitors.forms import AddCompetitorForm
from competition.controllers.competitors import competitors_bp

from competition.services.participation import ParticipationService


@competitors_bp.route('/view/all')
@login_required
def list_all():
    data = ParticipationService.read_all()
    return render_template('competitors/list.html')


@competitors_bp.route('/add/new', methods=['GET', 'POST'])
@login_required
def add_new():
    form = AddCompetitorForm()

    if form.validate_on_submit():
        comp = ParticipationService.create(form.name.data, form.surname.data, form.index_number.data, form.subject.data)

        if comp is None:
            flash('Nije moguće dodati takmičara.')
        else:
            flash('Takmičar uspješno dodan.')
            return render_template('competitors/list.html')

    return render_template('competitors/add_new.html', form=form)


# @competition_bp.route('/update/<name>/<date>', methods=['GET', 'POST'])
# @login_required
# def update(name, date):
#     comp = CompetitionService.read(name, date)
#     form = CreateCompetitionForm()
#
#     form.name.data = comp.name
#     form.date.date = str(comp.date)
#     form.subject.data = comp.field
#
#     if form.validate_on_submit():
#         CompetitionService.update(name, date, form.name.data, form.date.data, form.subject.data)
#         flash("Uspješna izmjena podataka")
#         return list_all()
#     else:
#         flash("Pogrešno uneseni podaci")
#
#     return render_template('competitors/add_new.html', form=form)


# @competition_bp.route('/delete/<name>/<date>')
# @login_required
# def delete(name, date):
#     CompetitionService.delete(name, date)
#     flash('Uspješno ste obrisali takmičara')
#     return list_all()
