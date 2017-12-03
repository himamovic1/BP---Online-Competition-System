from competition import Competition, db


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
    def read(name, date):
        return Competition.query.filter_by(name=name, date=date).first()

    @staticmethod
    def read_all():
        return Competition.query.all()

    @staticmethod
    def update(name, date, new_name, new_date, new_field_id):
        comp = CompetitionService.read(name, date)

        comp.name = new_name
        comp.date = new_date
        comp.field_id = new_field_id

        db.session.commit()

    @staticmethod
    def search(search_query):
        result = Competition.query.filter(Competition.name.ilike('%' + search_query.lower() + '%')).all()
        #result = result.order_by(Competition.name).all()
        return result

    @staticmethod
    def delete(name, date, commit=True):
        comp = CompetitionService.read(name, date)

        if comp:
            db.session.delete(comp)
        else:
            raise Exception("Given user does not exist")

        if commit:
            db.session.commit()
