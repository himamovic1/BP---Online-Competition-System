from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from competition.services.field import FieldService


class CreateCompetitionForm(FlaskForm):

    name = StringField(
        'Naziv takmičenja:',
        validators=[DataRequired()]
    )

    date = StringField(
        'Datum održavanja:',
        validators=[DataRequired()]
    )

    time = StringField(
        'Vrijeme održavanja',
        validators=[DataRequired()]
    )

    subject = QuerySelectField(
        'Oblast:',
        validators=[DataRequired()],
        query_factory=FieldService.read_all,
        get_pk=lambda f: f.id,
        get_label=lambda f: f.name
    )

    submit = SubmitField('Kreiraj')


class RegisterCompetitionResults(FlaskForm):
    name = StringField('Enter sentence', validators=[DataRequired()])
    import_file = FileField('Upload a file', validators=[DataRequired()])
    submit = SubmitField('Upload')
