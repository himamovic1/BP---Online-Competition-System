from competition import db

class Field(db.Model):
	__tablename__ = 'field'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), unique=True, nullable=False)

	def __init__(self, name):
		self.name = name