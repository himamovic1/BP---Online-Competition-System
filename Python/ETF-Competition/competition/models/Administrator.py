from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from competition import db
from competition.models import Ownership
from competition.models.User import User

class Administrator(User):
	__tablename__ = 'administrator'

	user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
	position = db.Column(db.String(255), nullable=False)
	competitions = relationship("Ownership")

	__mapper_args__ = {
		'polymorphic_identity': 'administrator',
	}

	def __init__(self, name, surname, email, position):
		super(Administrator, self).__init__(name, surname, email)
		self.position = position