from competition import db

Ownership = db.Table(
    'ownership',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey("administrator.user_id")),
    db.Column('competition_name', db.String(255)),
    db.Column('competition_date', db.DateTime),
    db.ForeignKeyConstraint(
        ['competition_name', 'competition_date'],
        ['competition.name', 'competition.date']
    )
)
