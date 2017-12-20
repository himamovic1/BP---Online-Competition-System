from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from wtforms import ValidationError

from competition.controllers.auth import auth_bp
from competition.controllers.auth.forms import LoginForm, RegistrationForm
from competition.services.auth import AuthService


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        if AuthService.login(login_form.email.data, login_form.password.data):
            return redirect(request.args.get('next') or url_for('competition.list_all'))
        else:
            flash('Invalid credentials')

    return render_template('auth/login.html', form=login_form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()

    try:
        if register_form.validate_on_submit() and register_form.validate_email():
            new_student = register_form.create_student()
            AuthService.register_student(new_student)
            flash('Aktivacijski mail poslan na Vašu adresu', category='success')
            return redirect(url_for('public.index'))

        elif request.method == 'POST':
            flash('Greška pri unosu podataka', category='error')

    except ValidationError as ve:
        flash('Pogrešno uneseni podaci: {}'.format(ve), category='error')
    except Exception as e:
        flash('Došlo je do greške', category='error')

    return render_template('auth/registration.html')

@auth_bp.route('/logout')
@login_required
def logout():
    AuthService.logout()
    flash('Uspješno ste se odjavili.')
    return redirect('/')

