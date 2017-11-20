from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from competition import db


class Competition(db.Model):
    __tablename__ = 'competition'

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    field_id = db.Column(db.Integer, ForeignKey("field.id"))
    # field = relationship("Field", backref=db.backref("competition"), uselist=False)
    questions = relationship("Question")

    def __init__(self, name, date, field_id):
        self.name = name
        self.date = date
        self.field_id = field_id

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}