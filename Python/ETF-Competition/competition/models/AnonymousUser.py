from flask_login import AnonymousUserMixin, login_manager

from competition import Permission


class AnonymousUser(AnonymousUserMixin):
    """ Helper class for anonymous users. """

    role = Permission.PUBLIC_ACCESS

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser