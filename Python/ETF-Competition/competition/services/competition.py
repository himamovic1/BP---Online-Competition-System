from competition import Competition, Field, db


class CompetitionService:
    """ Service class that deals with CRUD operations for Competition objects """

    @staticmethod
    def create(name, date, field, commit=True):
        # subject = Field.query.filter_by(id=field_id).first()

        comp = Competition(name=name, date=date, field_id=field.id)
        comp.field = field

        db.session.add(comp)

        if commit:
            db.session.commit()

        return comp

    @staticmethod
    def read(competition_id):
        return Competition.query.filter_by(id=competition_id)

    def update(self):
        pass

    @staticmethod
    def delete(competition_id, commit=True):
        comp = Competition.query.filter_by(id=competition_id)

        if comp:
            db.session.delete(comp)
        else:
            raise Exception("Given user does not exist")

        if commit:
            db.session.commit()
