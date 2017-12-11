from flask_login import current_user

from competition import Competition, db, Administrator


class CompetitionService:
    """ Service class that deals with CRUD operations for Competition objects """

    @staticmethod
    def create(**kwargs):
        # subject = Field.query.filter_by(id=field_id).first()

        comp = Competition(name=kwargs['name'], date=kwargs['date'], field_id=kwargs['field'].id)
        comp.field = kwargs['field']

        return CompetitionService.add(comp, kwargs.get('commit', False))

    @staticmethod
    def create_from_object(comp, commit=False):
        if comp is not None:
            comp.owners.append(Administrator.query.filter_by(user_id=current_user.id).first())
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
    def read_mine():
        admin = Administrator.query.filter_by(user_id=current_user.id).first()
        return admin.competitions

    @staticmethod
    def update(comp, comp_form, commit=False):
        comp_form.refresh_competition(comp)

        if commit:
            db.session.commit()

    @staticmethod
    def search(search_query):
        result = Competition.query.filter(Competition.name.ilike('%' + search_query.lower() + '%')).all()
        #result = result.order_by(Competition.name).all()
        return result

    @staticmethod
    def delete(name, date, commit=False):
        comp = CompetitionService.read(name, date)

        if comp:
            db.session.delete(comp)
        else:
            raise Exception("Given user does not exist")

        if commit:
            db.session.commit()

