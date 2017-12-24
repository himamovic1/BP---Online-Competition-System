from flask import current_app
from flask_login import login_user, logout_user

from competition import User, Student, Administrator, db


class AuthService:
    """ Class wrapping the authentication process. """

    @staticmethod
    def login(email, password, _internal=False):

        # Get the user
        user = User.query.filter_by(email=email).first()

        check_password = True
        if not _internal:
            check_password = user.verify_password(password)

        # If the credentials are okay log user in and return True
        if user is not None and check_password:
            login_user(user)
            return True

        return False

    @staticmethod
    def register_student(new_student):
        db.session.add(new_student)
        db.session.commit()
        AuthService.send_activation_email(new_student)
        AuthService.login(new_student.email, password='', _internal=True)

    @staticmethod
    def logout():
        logout_user()

    @staticmethod
    def send_activation_email(student):
        from competition.utils import send_email

        send_email(sender=current_app.config.get('MAIL_ADMIN'),
                   recipients=[student.email],
                   subject='Aktivacija korisničkog računa | ETF Competition',
                   template='auth/email.html',
                   name=student.name,
                   token=student.generate_confirmation_token())
