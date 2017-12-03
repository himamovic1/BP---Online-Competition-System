from sqlalchemy import ForeignKey

from competition import db


class Question(db.Model):
    __tablename__ = 'question'

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['competition_name', 'competition_date'],
            ['competition.name', 'competition.date']
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    ordinal_number = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Float, nullable=False)
    competition_name = db.Column(db.String(255))
    competition_date = db.Column(db.DateTime)

    def __init__(self, text, ordinal_number, max_score, competition_name, competition_date):
        self.text = text
        self.ordinal_number = ordinal_number
        self.max_score = max_score
        self.competition_name = competition_name
        self.competition_date = competition_date
