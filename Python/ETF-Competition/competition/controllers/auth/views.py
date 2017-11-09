from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user

from competition import User
from competition.controllers.auth import auth_bp
from competition.controllers.auth.forms import LoginForm


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('competition.competition_list'))

        flash('Invalid credentials')
    return render_template('auth/login.html', form=login_form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out.')
    return render_template('index.html')
