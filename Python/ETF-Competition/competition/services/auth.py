from flask_login import login_user, logout_user

from competition import User, Student, Administrator, db


class AuthService:
    """ Class wrapping the authentication process. """

    @staticmethod
    def login(email, password):

        # Get the user
        user = User.query.filter_by(email=email).first()

        # If the credentials are okay log user in and return True
        if user is not None and user.verify_password(password):
            login_user(user)
            return True

        return False

    @staticmethod
    def register_student(new_student, commit=False):
        db.session.add(new_student)

        if commit:
            db.session.commit()

    @staticmethod
    def logout():
        logout_user()

    @staticmethod
    def send_activation_email(user):
        send_email(user.email, 'Aktivacija profila', 'auth/email/confirmation', user=user)
