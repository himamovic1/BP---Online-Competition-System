import os
from flask import render_template, flash, request, jsonify
from flask_login import login_required

from competition.controllers.competition import competition_bp
from competition.controllers.competition.forms import CreateCompetitionForm, RegisterCompetitionResults
from competition.decorators import admin_required
from competition.services.competition import CompetitionService


@competition_bp.route('/view/all')
@login_required
def list_all():
    data = CompetitionService.read_all()
    return render_template('competition/list.html', competition_list=data)


@competition_bp.route('/view/calendar')
@login_required
def calendar():
    return render_template('competition/calendar.html')


@competition_bp.route('/add/new', methods=['GET', 'POST'])
@login_required
def add_new():
    form = CreateCompetitionForm()

    if form.validate_on_submit():
        comp = CompetitionService.create(form.name.data, form.date.data, form.subject.data)

        if comp is None:
            flash('Nije moguće dodati takmičenje.')
        else:
            flash('Uspješno ste kreirali takmičenje.')
            return render_template('competition/list.html')

    return render_template('competition/add_new.html', form=form)


@competition_bp.route('/update/<name>/<date>', methods=['GET', 'POST'])
@login_required
def update(name, date):
    comp = CompetitionService.read(name, date)
    form = CreateCompetitionForm()

    form.name.data = comp.name
    form.date.date = str(comp.date)
    form.subject.data = comp.field

    if form.validate_on_submit():
        CompetitionService.update(name, date, form.name.data, form.date.data, form.subject.data)
        flash("Uspješna izmjena podataka")
        return list_all()
    else:
        flash("Pogrešno uneseni podaci")

    return render_template('competition/add_new.html', form=form)


@competition_bp.route('/delete/<name>/<date>')
@login_required
def delete(name, date):
    CompetitionService.delete(name, date)
    flash('Uspješno ste obrisali takmičenje')
    return list_all()


@competition_bp.route('/results/upload/<name>/<date>', methods=['GET'])
@login_required
def get_plugin_form(name, date):
    form = RegisterCompetitionResults()
    return render_template('competition/upload_results.html', form=form)


@competition_bp.route('/results/upload', methods=['POST'])
@login_required
def upload_results():

    file = request.files.getlist('file')[0]
    if file:
        file.save(os.path.join(os.getcwd(), 'storage', 'uploads', file.filename))
        print(file.filename)

        resp = jsonify({'upload': 'success'})
        return resp

    flash('Something went wrong')
    resp = jsonify({'error': 'Oh snap! An error occured.'})
    return resp





