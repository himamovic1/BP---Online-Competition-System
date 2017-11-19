from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from competition import db, login_manager


class ETFUser(UserMixin, db.Model):
		__bindkey__ = 'etfdb'
		__tablename__ = 'users'

		id = db.Column(db.Integer, primary_key=True, index=True)
		username = db.Column(db.String(255), nullable=False, unique=True, index=True)
		pwHash = db.Column(db.String(255), index=True)
		isPwChanged = db.Column(db.Integer)
		mail = db.Column(db.String(50), nullable=True)

		def __init__(self, username, isPwChanged, mail):
			self.username = username
			self.isPwChanged = isPwChanged
			self.mail = mail

		@property
		def password(self):
			raise AttributeError('Password is not a readable attribute')

		@password.setter
		def password(self, pw):
			self.pwHash = generate_password_hash(pw)

		def verify_password(self, pw):
			return check_password_hash(self.pwHash, pw)

		def __repr__(self):
			return '<User: %r>' % self.username

@login_manager.user_loader
def load_user(uid):
	return User.query.get(int(uid))