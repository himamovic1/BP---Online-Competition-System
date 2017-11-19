from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user

from competition import User
from competition.controllers.auth import auth_bp
from competition.controllers.auth.forms import LoginForm
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


@auth_bp.route('/logout')
@login_required
def logout():
    AuthService.logout()
    flash('Uspješno ste se odjavili.')
    return redirect('/')

