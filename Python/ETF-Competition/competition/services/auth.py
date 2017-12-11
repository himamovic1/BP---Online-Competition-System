from flask_login import login_user, logout_user

from competition import User, Student, Administrator


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
    def logout():
        logout_user()
