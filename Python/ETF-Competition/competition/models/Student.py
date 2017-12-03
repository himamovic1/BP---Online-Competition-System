from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from competition import db
from competition.models import Participation
from competition.models.User import User


class Student(User):
	__tablename__ = 'student'

	user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
	index_number = db.Column(db.String(255), unique=True, nullable=False)
	study_year = db.Column(db.Integer, nullable=False)
	competitions = relationship("Participation")

	__mapper_args__ = {
		'polymorphic_identity': 'student',
	}

	def __init__(self, name, surname, email, index_number, study_year):
		super(Student, self).__init__(name, surname, email)
		self.index_number = index_number
		self.study_year = study_year

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}