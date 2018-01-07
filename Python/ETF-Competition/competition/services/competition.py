import os
from pathlib import Path

from flask_login import current_user
from sqlalchemy import func, and_
from sqlalchemy.sql import label

from competition import Competition, db, Administrator, Result, Participation, Student, Field


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
        if current_user.is_administrator():
            user = Administrator.query.filter_by(user_id=current_user.id).first()
            return user.competitions
        else:
            return Competition.query.filter(Competition.name == Participation.competition_name) \
                .filter(Competition.date == Participation.competition_date) \
                .filter(Participation.user_id == current_user.id).all()

    @staticmethod
    def read_all_results(name, date):
        return db.session.query(Student, Result).filter(Result.participation_id == Participation.id) \
            .filter(Participation.user_id == Student.user_id) \
            .filter(Participation.competition_name == name)\
        .filter(Participation.competition_date == date).all()

    @staticmethod
    def update(comp, comp_form, commit=False):
        comp_form.refresh_competition(comp)

        if commit:
            db.session.commit()

    @staticmethod
    def search(search_query):
        query = Competition.query
        if search_query:
            query = query.filter(Competition.name.ilike('%' + search_query.lower() + '%'))
        result = query.all()
        # result = result.order_by(Competition.name).all()
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

    @staticmethod
    def save_results_to_db(results_file_name, competition_name, competition_date):
        import csv

        try:
            with open('storage/uploads/' + results_file_name, 'r') as csvfile:
                results_reader = csv.DictReader(csvfile)

                for result in results_reader:
                    indexnumber = result['broj_indeksa']
                    points_scored = result['broj_bodova']

                    user = Student.query.filter_by(index_number=indexnumber).first()
                    participation = Participation.query.filter(Participation.user_id == user.user_id) \
                        .filter(Participation.competition_date == competition_date) \
                        .filter(Participation.competition_name == competition_name).first()

                    old_res = Result.query.filter_by(participation_id=participation.id).first()
                    if old_res:
                        old_res.points_scored = points_scored
                    else:
                        p = Result(participation.id, points_scored)
                        db.session.add(p)

                db.session.commit()
                file_path = os.path.join('storage', 'uploads', results_file_name)
                old_file = Path(file_path)

                if old_file.is_file():
                    os.remove(file_path)
        except OSError:
            return True
        except Exception:
            db.session.rollback()
            raise Exception('Greška prilikom učitavanja rezultata.')

    @staticmethod
    def competitor_overall_score(user_id):
        return db.session.query(Field.name, Competition.name, label('points', func.max(Result.points_scored))) \
            .group_by(Field.id, Competition.name) \
            .filter(Field.id == Competition.field_id) \
            .filter(and_(Competition.name == Participation.competition_name,
                         Competition.date == Participation.competition_date)) \
            .filter(Participation.id == Result.participation_id) \
            .filter(Participation.user_id == user_id) \
            .all()

    @staticmethod
    def points_per_competition(user_id):
        return db.session.query(Field.name, label('count', func.count(Participation.id))) \
            .group_by(Field.id) \
            .filter(Field.id == Competition.field_id) \
            .filter(and_(Competition.name == Participation.competition_name,
                         Competition.date == Participation.competition_date)) \
            .filter(Participation.user_id == user_id) \
            .all()

    @staticmethod
    def max_points_per_field(user_id):
        return db.session.query(Field.name, label('maximum', func.max(Result.points_scored))) \
        .group_by(Field.id) \
        .filter(Field.id == Competition.field_id) \
        .filter(and_(Competition.name == Participation.competition_name, Competition.date == Participation.competition_date)) \
        .filter(Participation.id == Result.participation_id) \
        .filter(Participation.user_id == user_id) \
        .all()