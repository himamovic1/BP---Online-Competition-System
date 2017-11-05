from competition import db


class test(db.Model):
	__tablename__ = 'test'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))

	def __init__(self, name):
		self.name = name
