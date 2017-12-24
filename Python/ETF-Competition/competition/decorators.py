from functools import wraps
from threading import Thread

from flask import abort, url_for, redirect, request
from flask_login import current_user

from competition import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator

def confirmation_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.confirmed:
                return redirect(url_for('auth.unconfirmed'))
            else:
                return f(*args, **kwargs)

        return decorated_function

    return decorator

def admin_required(f):
    return permission_required(Permission.FULL_ACCESS)(f)

def student_required(f):
    return permission_required(Permission.STUDENT_ACCESS)(f)

def async(f):
    """ Decorator to make the function run in the new thread. """
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper

