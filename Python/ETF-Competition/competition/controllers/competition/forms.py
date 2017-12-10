from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Regexp

from competition import Competition
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

    # time = StringField(
    #     'Vrijeme održavanja',
    #     validators=[
    #         DataRequired(),
    #         Regexp('\d{1,2}:\d{2}', message="Vrijeme mora biti u formatu hh:mm")
    #     ],
    #     default='12:00'
    # )

    subject = QuerySelectField(
        'Oblast:',
        validators=[DataRequired()],
        query_factory=FieldService.read_all,
        get_pk=lambda f: f.id,
        get_label=lambda f: f.name
    )

    submit = SubmitField('Kreiraj')

    # Fill form with a competition
    def put_competition(self, comp):
        self.name.data = comp.name
        self.date.data = comp.date
        self.subject.data = comp.field

    # Create Competition object from form data
    def pop_competition(self):
        comp = None

        if self.validate():
            comp = Competition(
                name=self.name.data,
                date=self.date.data,
                field_id=self.subject.data.id
            )

            comp.field = self.subject.data

        return comp

    # Update competition object with new data
    def refresh_competition(self, comp):
        comp.name = self.name.data,
        comp.date = self.date.data,
        comp.field_id = self.subject.data.id
        comp.field = self.subject.data

    # Update the label according to te usage of form
    def set_create_mode(self):
        self.submit.label.text = 'Kreiraj'

    def set_edit_mode(self):
        self.submit.label.text = 'Spasi izmjene'


class RegisterCompetitionResults(FlaskForm):
    name = StringField('Enter sentence', validators=[DataRequired()])
    import_file = FileField('Upload a file', validators=[DataRequired()])
    submit = SubmitField('Upload')
