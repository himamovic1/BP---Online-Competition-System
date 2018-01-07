import os

from flask import render_template, flash, request, redirect, url_for, abort, current_app, session, jsonify
from flask_login import login_required, current_user

from competition.controllers.competition import competition_bp
from competition.controllers.competition.forms import CreateCompetitionForm, CompetitionFormBase
from competition.decorators import admin_required, student_required
from competition.services.competition import CompetitionService

#################################################
# Read region                                   #
#################################################
from competition.services.student import StudentService


@competition_bp.route('/view/single/<name>/<date>', methods=['GET'])
def list_one(name, date):
    participations = StudentService.search_by_competition_participation(competition_name=name, competition_date=date)

    results = CompetitionService.read_all_results(name=name, date=date)
    res_count = len(results)

    if res_count > 0:
        has_results = True
    else:
        has_results = False

    comp = CompetitionService.read(name, date)

    if current_user.is_administrator():
        form = CreateCompetitionForm()
        form.initialize_fields()
    else:
        form = CompetitionFormBase()

    form.put_competition(comp)
    form.set_read_only_mode()
    return render_template('competition/single_view.html', form=form, showParticipations=0,
                           participations=participations, name=comp.name, date=comp.date, has_results=has_results)


@competition_bp.route('/view/mine')
@login_required
def list_mine():
    data = CompetitionService.read_mine()
    return render_template('competition/list_view.html', competition_list=data)


@competition_bp.route('/view/all')
def list_all():
    data = CompetitionService.read_all()
    return render_template('competition/list_view.html', competition_list=data)


@competition_bp.route('/view/statistics/<name>/<date>', methods=['GET'])
def show_stats(name, date):
    results = CompetitionService.read_all_results(name=name, date=date)
    keys = [i for i in range(21)]
    res_dict = dict.fromkeys(keys, 0)
    num_passed = 0
    num_failed = 0
    p = 0
    results_count = len(results)

    if results_count == 0:
        flash("Nema rezultata takmičenja.")
    else:
        for result in results:
            if result[1].points_scored >= 10:
                num_passed += 1
            else:
                num_failed += 1

            res_dict[int(result[1].points_scored)] += 1
        p = num_passed / results_count * 100

    return render_template('competition/competition_statistics.html', res_dict=res_dict, results_count=results_count,
                           passed=p, num_passed=num_passed, num_failed=num_failed)


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


@competition_bp.route('/results/save/<name>/<date>', methods=['GET'])
@login_required
@admin_required
def submit_results(name, date):
    comp = CompetitionService.read(name, date)

    try:
        file_name = session.pop('result_file')
        CompetitionService.save_results_to_db(file_name, name, date)

        flash('Upload rezultata uspješan')
        return redirect(url_for('competition.list_mine'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('competition.upload_results', name=name, date=date))


@competition_bp.route('/results/upload/<name>/<date>', methods=['GET', 'POST'])
@login_required
@admin_required
def upload_results(name, date):
    if request.method == 'POST' and request.files.getlist('file'):
        file = request.files.getlist('file')[0]
        if file:
            file_path = os.path.join(os.getcwd(), 'storage', 'uploads', file.filename)

            try:
                if not file_path.endswith('.csv'):
                    raise Exception('Datoteka sa rezultatima mora biti u CSV formatu.')

                file.save(file_path)
                session['result_file'] = file.filename

                return jsonify({'message': 'Upload uspješan'})
            except Exception as e:
                return jsonify({'error': 'Greška prilikom uploada'})
    else:
        comp = CompetitionService.read(name, date)
        return render_template('competition/upload_results_view.html', comp=comp)


@competition_bp.route('/results/view/<name>/<date>')
def view_results(name, date):
    results = CompetitionService.read_all_results(name=name, date=date)
    return render_template('competition/view_results.html', results=results)


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
    from competition.services.participation import ParticipationService
    p = ParticipationService.sign_up(current_user.id, name, date, commit=True)

    if p:
        flash('Uspješno ste prijavljeni na takmičenje', 'success')
        return redirect(url_for('competition.list_mine'))
    else:
        flash('Greška prilikom prijave', 'warning')
        return redirect(url_for('competition.list_all'))


