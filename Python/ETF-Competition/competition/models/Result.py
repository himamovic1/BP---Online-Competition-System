from sqlalchemy.orm import relationship

from competition import db


class Result(db.Model):
    __tablename__ = 'result'

    participation_id = db.Column(db.Integer, db.ForeignKey('participation.id'), primary_key=True)
    participation = relationship("Participation", backref=db.backref("result", uselist=False))
    points_scored = db.Column(db.Float, nullable=False)

    def __init__(self, participation_id, points_scored):
        self.participation_id = participation_id
        self.points_scored = points_scored
