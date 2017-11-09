from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from competition import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), index=True)
    type = db.Column(db.String(50), nullable=False)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def verify_password(self, pw):
        return check_password_hash(self.password_hash, pw)

    def __repr__(self):
        return '<User: %r>' % self.name

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }


@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))
