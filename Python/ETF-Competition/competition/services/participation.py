from competition import db, Student, Participation


class ParticipationService:
    """ Service class that deals with CRUD operations for Participations """

    @staticmethod
    def create(user_id, competition_name, competition_date, commit=True):

        participation = Participation(user_id=user_id, competition_name=competition_name, competition_date=competition_date)

        db.session.add(participation)

        if commit:
            db.session.commit()

        return participation

    @staticmethod
    def read(user_id, competition_name, competition_date):
        return Participation.query.filter_by(user_id, competition_name, competition_date).first()

    @staticmethod
    def read_all():
        return Participation.query.all()

    # @staticmethod
    # def update(name, date, new_name, new_date, new_field_id):
    #     comp = Participation.read(name, date)
    #
    #     comp.name = new_name
    #     comp.date = new_date
    #     comp.field_id = new_field_id
    #
    #     db.session.commit()

    # @staticmethod
    # def search(search_query):
    #     result = Competition.query.filter(Competition.name.ilike('%' + search_query.lower() + '%')).all()
    #     #result = result.order_by(Competition.name).all()
    #     return result

    @staticmethod
    def delete(user_id, competition_name, competition_date, commit=True):
        participation = ParticipationService.read(user_id, competition_name, competition_date)

        if participation:
            db.session.delete(participation)
        else:
            raise Exception("Given user does not exist")

        if commit:
            db.session.commit()
