from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired


class AddCompetitorForm(FlaskForm):

    name = StringField(
        'Ime takmičara',
        validators=[DataRequired()]
    )

    surname = StringField(
        'Prezime takmičara',
        validators=[DataRequired()]
    )

    index_number = StringField(
        'Broj indeksa',
        validators=[DataRequired()]
    )

    year = StringField(
        'Godina studija',
        validators=[DataRequired()]
    )

    competition_name = StringField(
        '',
        id='competition_name',
        validators=[DataRequired()]
    )
    competition_date = StringField(
        '',
        id='competition_date',
        validators=[DataRequired()]
    )

    submit = SubmitField('Dodaj takmičara')
