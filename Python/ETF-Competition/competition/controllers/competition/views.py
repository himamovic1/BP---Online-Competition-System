import os

from flask import render_template, flash, request, redirect, url_for, abort
from flask_login import login_required, current_user

from competition.controllers.competition import competition_bp
from competition.controllers.competition.forms import CreateCompetitionForm
from competition.decorators import admin_required, student_required
from competition.services.competition import CompetitionService


#################################################
# Read region                                   #
#################################################
from competition.services.student import StudentService


@competition_bp.route('/view/single/<name>/<date>', methods=['GET'])
@login_required
def list_one(name, date):
    participations = StudentService.search_by_competition_participation(competition_name=name, competition_date=date)

    comp = CompetitionService.read(name, date)
    form = CreateCompetitionForm()
    form.initialize_fields()
    form.put_competition(comp)
    form.set_read_only_mode()
    return render_template('competition/single_view.html', form=form, showParticipations=0, participations=participations)


@competition_bp.route('/view/mine')
@login_required
@admin_required
def list_mine():
    data = CompetitionService.read_mine()
    return render_template('competition/list_view.html', competition_list=data)


@competition_bp.route('/view/all')
@login_required
def list_all():
    data = CompetitionService.read_all()
    return render_template('competition/list_view.html', competition_list=data)


#################################################
# Create, Update and Delete region              #
#################################################
@competition_bp.route('/add/new', methods=['GET', 'POST'])
@login_required
@admin_required
def add_new():
    form = CreateCompetitionForm()
    form.initialize_fields()
    form.set_create_mode()

    if form.editable and form.validate_on_submit():
        comp = CompetitionService.create_from_object(form.pop_competition(), commit=True)

        if comp is None:
            flash('Nije moguće kreirati takmičenje.')
        else:
            flash('Uspješno ste kreirali takmičenje.')
            return redirect(url_for('competition.list_all'))

    return render_template('competition/add_new.html', form=form, isEdit=0)


@competition_bp.route('/update/<name>/<date>', methods=['GET', 'POST'])
@login_required
@admin_required
def update(name, date):
    comp = CompetitionService.read(name, date)
    form = CreateCompetitionForm()
    form.initialize_fields()
    form.set_edit_mode()

    # Check if competition can be editable
    if not comp.is_editable(current_user.id):
        abort(403)

    if request.method == 'GET':
        form.put_competition(comp)

    elif form.editable and form.validate_on_submit():
        CompetitionService.update(comp, form, commit=True)
        flash("Uspješna izmjena podataka")
        return redirect(url_for('competition.list_all'))

    else:
        flash("Pogrešno uneseni podaci")

    return render_template('competition/add_new.html', form=form, isEdit=1)


@competition_bp.route('/results/upload/<name>/<date>', methods=['GET', 'POST'])
@login_required
@admin_required
def upload_results(name, date):

    if request.method == 'POST':
        file = request.files.getlist('file')[0]
        if file:
            file.save(os.path.join(os.getcwd(), 'storage', 'uploads', file.filename))
            flash('Upload rezultata uspješan')
            return redirect(url_for('competition.list_mine'))
        else:
            flash('Upload rezultata nije moguć trenutno')

    comp = CompetitionService.read(name, date)
    return render_template('competition/upload_results_view.html', comp=comp)


@competition_bp.route('/delete/<name>/<date>')
@login_required
@admin_required
def delete(name, date):
    CompetitionService.delete(name, date)
    flash('Uspješno ste obrisali takmičenje')
    return redirect(url_for('competition.list_all'))


#################################################
# Sign up region                                #
#################################################
@competition_bp.route('/sign/<name>/<date>')
@login_required
@student_required
def sign_up(name, date):
    raise NotImplemented()
