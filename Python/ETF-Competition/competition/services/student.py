from competition import db, Student, User, Participation
from sqlalchemy import or_, and_

class StudentService:

    @staticmethod
    def read(user_id):
        return Student.query.filter_by(user_id=user_id).first()

    @staticmethod
    def read_all():
        return Student.query.all()

    @staticmethod
    def update(name, surname, email, study_year, index_number, new_name, new_surname, new_email, new_study_year,
               new_index_number):
        stud = StudentService.read(index_number)

        stud.name = new_name
        stud.surname = new_surname
        stud.email = new_email
        stud.study_year = new_study_year
        stud.index_number = new_index_number

        db.session.commit()

    @staticmethod
    def search(search_query):
        result = Student.query.filter(Student.name.ilike('%' + search_query.lower() + '%')).all()
        # result = result.order_by(Competition.name).all()
        return result

    @staticmethod
    def search_by_attributes(name, surname, index, study_year):
        result = []

        if (study_year == ''):
            result = Student.query.filter(and_(
                Student.name.ilike('%' + name.lower() + '%'),
                Student.surname.ilike('%' + surname.lower() + '%'),
                Student.index_number.ilike('%' + index.lower() + '%')
            )).all()
        else:
            result = Student.filter(and_(
                Student.name.ilike('%' + name.lower() + '%'),
                Student.surname.ilike('%' + surname.lower() + '%'),
                Student.index_number.ilike('%' + index.lower() + '%')
            )).filter_by(study_year=study_year).all()

        return result

    @staticmethod
    def search_by_competition_participation(competition_name, competition_date):
        return Student.query.filter(Participation.competition_date == competition_date).\
	    filter(Participation.competition_name == competition_name).\
        filter(Student.user_id == Participation.user_id).all()

    @staticmethod
    def delete(index_number, commit=True):
        comp = StudentService.read(index_number=index_number)

        if comp:
            db.session.delete(comp)
        else:
            raise Exception("Given user does not exist")

        if commit:
            db.session.commit()
