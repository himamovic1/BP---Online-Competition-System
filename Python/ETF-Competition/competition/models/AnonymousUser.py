from flask_login import AnonymousUserMixin, login_manager


class AnonymousUser(AnonymousUserMixin):
    """ Helper class for anonymous users. """

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser