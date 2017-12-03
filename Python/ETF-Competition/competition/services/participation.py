from competition import db, Student, Participation


class ParticipationService:
    """ Service class that deals with CRUD operations for Participations """

    @staticmethod
    def create(name, surname, index_number, year, competition_date, competition_name, commit=True):
        usr = Student.query.filter_by(index_number=index_number).first()
        participation = Participation(user_id=usr.user_id, competition_name=competition_name, competition_date=competition_date)

        db.session.add(participation)

        if commit:
            db.session.commit()

        return participation

    @staticmethod
    def read(id):
        return Participation.query.filter_by(id=id).first()

    @staticmethod
    def read_all():
        return Participation.query.all()

    @staticmethod
    def update(id, name, surname, index_number, new_index_number, year, competition_name, competition_date):
        usr = Student.query.filter_by(index_number=index_number)
        usr.name = name
        usr.surname = surname
        usr.index_number = new_index_number
        usr.year = year

        comp = Participation.read(id=id)
        comp.user_id = usr.user_id
        comp.competition_name = competition_name
        comp.competition_date = competition_date

        db.session.commit()

    # @staticmethod
    # def search(search_query):
    #     result = Competition.query.filter(Competition.name.ilike('%' + search_query.lower() + '%')).all()
    #     #result = result.order_by(Competition.name).all()
    #     return result

    # @staticmethod
    # def delete(user_id, competition_name, competition_date, commit=True):
    #     participation = ParticipationService.read(user_id, competition_name, competition_date)
    #
    #     if participation:
    #         db.session.delete(participation)
    #     else:
    #         raise Exception("Given user does not exist")
    #
    #     if commit:
    #         db.session.commit()
