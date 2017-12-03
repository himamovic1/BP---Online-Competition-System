from competition import db, Student


class StudentService:

    @staticmethod
    def read(user_id):
        return Student.query.filter_by(user_id = user_id).first()


    @staticmethod
    def read_all():
        return Student.query.all()

    @staticmethod
    def update(name, surname, email, study_year, index_number, new_name, new_surname, new_email, new_study_year, new_index_number):
        stud = StudentService.read(index_number)

        stud.name = new_name
        stud.surname = new_surname
        stud.email = new_email
        stud.study_year = new_study_year
        stud.index_number = new_index_number

        db.session.commit()

    @staticmethod
    def search(search_query):
        result = StudentService.query.filter(Student.name.ilike('%' + search_query.lower() + '%')).all()
        #result = result.order_by(Competition.name).all()
        return result

    @staticmethod
    def delete(index_number, commit=True):
        comp = StudentService.read(index_number=index_number)

        if comp:
            db.session.delete(comp)
        else:
            raise Exception("Given user does not exist")

        if commit:
            db.session.commit()
