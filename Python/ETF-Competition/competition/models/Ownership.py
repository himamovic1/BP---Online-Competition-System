from sqlalchemy import ForeignKey

from competition import db


class Ownership(db.Model):
    __tablename__ = 'ownership'

    __table_args__ = (
        db.ForeignKeyConstraint(
            ['competition_name', 'competition_date'],
            ['competition.name', 'competition.date']
        ),
    )

    user_id = db.Column(db.Integer, ForeignKey("administrator.user_id"), primary_key=True)
    competition_name = db.Column(db.String(255), primary_key=True)
    competition_date = db.Column(db.DateTime, primary_key=True)
