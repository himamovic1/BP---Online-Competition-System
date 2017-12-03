from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from competition import db


class Participation(db.Model):
    __tablename__ = 'participation'

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['competition_name', 'competition_date'],
            ['competition.name', 'competition.date']
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("student.user_id"))
    competition_name = db.Column(db.String(255))
    competition_date = db.Column(db.DateTime)

    def __init__(self, user_id, competition_name, competition_date):
        self.user_id = user_id
        self.competition_name = competition_name
        self.competition_date = competition_date

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
