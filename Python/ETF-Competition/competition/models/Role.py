from competition import db, Permission


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'Administrator': (Permission.FULL_ACCESS, False),
            'Student': (Permission.STUDENT_ACCESS, False),
            'Unknown': (Permission.BANNED_ACCESS, True)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()

            if role is None:
                role = Role(name=r)

            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)

        db.session.commit()
