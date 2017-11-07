from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from competition import db

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	surname = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	type = db.Column(db.String(50), nullable=False)

	__mapper_args__ = {
		'polymorphic_identity': 'user',
		'polymorphic_on': type
	}

	def __init__(self, name, surname, email):
		self.name = name
		self.surname = surname
		self.email = email