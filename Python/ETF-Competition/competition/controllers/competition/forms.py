from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Regexp

from competition import Competition, Administrator
from competition.services.field import FieldService

class CompetitionFormBase(FlaskForm):
    editable = True

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
        self.editable = True
        self.submit.label.text = 'Kreiraj'

    def set_edit_mode(self):
        self.editable = True
        self.submit.label.text = 'Spasi izmjene'

    def set_read_only_mode(self):
        self.editable = False

        for field in self._fields.values():
            field.render_kw = dict(readonly='true', disabled='true')


class CreateCompetitionForm(CompetitionFormBase):
    ensemble = QuerySelectMultipleField(
        'Administratori:',
        validators=[DataRequired()],
        get_pk=lambda f: f.id,
        get_label=lambda f: "{} {}".format(f.name, f.surname)
    )

    submit = SubmitField('Kreiraj')

    # Initialize fields with data available after startup
    def initialize_fields(self):
        self.ensemble.query_factory = Administrator.query.filter(Administrator.id != current_user.id).all

    # Fill form with a competition
    def put_competition(self, comp):
        super(CreateCompetitionForm, self).put_competition(comp)
        self.ensemble.data = comp.owners

    # Create Competition object from form data
    def pop_competition(self):
        comp = super(CreateCompetitionForm, self).pop_competition()
        comp.owners = self.ensemble.data
        return comp

    # Update competition object with new data
    def refresh_competition(self, comp):
        super(CreateCompetitionForm, self).refresh_competition(comp)
        comp.owners = self.ensemble.data

    def set_read_only_mode(self):
        super(CreateCompetitionForm, self).set_read_only_mode()
        self.submit.render_kw=dict(style="display:none;")