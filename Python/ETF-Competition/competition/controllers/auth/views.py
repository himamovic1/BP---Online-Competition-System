from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from wtforms import ValidationError

from competition.controllers.auth import auth_bp
from competition.controllers.auth.forms import LoginForm, RegistrationForm
from competition.services.auth import AuthService

@auth_bp.before_app_request
def before_request():
    from competition.utils import redirect_unconfirmed
    redirected = redirect_unconfirmed(current_user,
                                      allowed_endpoints=['auth.login',
                                                         'auth.logout',
                                                         'auth.unconfirmed',
                                                         'auth.confirm',
                                                         'auth.resend'])

    if redirected:
        return redirected

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

    if request.method == 'POST':
        try:
            if register_form.validate_on_submit():
                new_student = register_form.create_student()
                AuthService.register_student(new_student)
                flash('Aktivacijski mail poslan na Vašu adresu', category='success')
                return redirect(url_for('public.index'))

            elif request.method == 'POST':
                flash('Greška pri unosu podataka', category='error')

        except ValidationError as ve:
            flash('Pogrešno uneseni podaci: {}'.format(ve), category='error')
        except Exception as e:
            flash('Došlo je do greške: {}'.format(str(e)), category='error')

    return render_template('auth/registration.html', form=register_form)


@auth_bp.route('/confirm/<string:token>', methods=['GET'])
@login_required
def confirm(token):
    from flask_login import current_user

    if current_user.confirmed:
        flash('Vaš račun je već aktiviran')
    elif current_user.confirm_student(token):
        flash('Uspješno ste aktivirali svoj korisnički račun')
    else:
        flash('Link za aktivaciju nije ispravan ili je istekao.')

    return redirect(url_for('public.index'))


@auth_bp.route('/resend', methods=['GET'])
def resend():
    from flask import current_app
    app = current_app
    try:
        AuthService.send_activation_email(current_user)
        flash('Aktivacijski mail poslan na Vašu adresu', category='success')
    except Exception as e:
        flash('Došlo je do greške: {}'.format(str(e)), category='error')

    return redirect(url_for('public.index'))


@auth_bp.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('public.index'))

    return render_template('auth/unconfirmed.html')


@auth_bp.route('/logout')
@login_required
def logout():
    AuthService.logout()
    flash('Uspješno ste se odjavili.')
    return redirect('/')

