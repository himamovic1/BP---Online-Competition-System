from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from competition import db, Role, Permission
from competition.models import Participation
from competition.models.User import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Student(User):
    __tablename__ = 'student'

    user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    index_number = db.Column(db.String(255), unique=True, nullable=False)
    study_year = db.Column(db.Integer, nullable=False)
    participations = relationship("Participation")
    confirmed = db.Column(db.Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

    def __init__(self, name, surname, email, index_number, study_year):
        super(Student, self).__init__(name, surname, email, 'student')
        self.index_number = index_number
        self.study_year = study_year
        self.confirmed = False
        self.role = Role.query.filter_by(permissions=Permission.STUDENT_ACCESS).first()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def is_administrator(self):
        return False

    # Registration related section
    def generate_confirmation_token(self, expiration=3600):
        from flask import current_app
        s = Serializer(current_app.config.get('SECRET_KEY', 'secret_key'), expiration)
        return s.dumps(dict(confirm=self.user_id))

    def confirm_student(self, token):
        from flask import current_app
        s = Serializer(current_app.config.get('SECRET_KEY', 'secret_key'))

        try:
            data = s.loads(token)
        except:
            return False

        if data.get('confrim') != self.user_id:
            return False

        self.confirmed = True
        db.session.commit()
        return True

