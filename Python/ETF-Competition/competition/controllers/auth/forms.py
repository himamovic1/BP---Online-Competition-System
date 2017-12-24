from flask import current_app
from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Prijava')

class RegistrationForm(FlaskForm):
    name = StringField('Ime',
                       validators=[DataRequired(),
                                   Length(1, 64),
                                   Regexp(r'^[A-Za-z][A-Za-z0-9_.]{1,64}$',
                                          message="Ime smije sadržavati samo slova, donju crtu i tačku")])

    surname = StringField('Prezime',
                       validators=[DataRequired(),
                                   Length(1, 64),
                                   Regexp(r'^[A-Za-z][A-Za-z0-9_.]{1,64}$',
                                          message="Prezime smije sadržavati samo slova, donju crtu i tačku")])

    index = StringField('Broj indeksa',
                        validators=[DataRequired(),
                                    Regexp(r'^\d{1,5}$',
                                           message='Broj indeksa ne smije sadžavati slova, te mora biti dužine do 5 cifri.')])

    study_year = IntegerField('Godina studija',
                              validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(1, 64),
                                    Email()])

    password = PasswordField('Lozinka',
                             validators=[DataRequired()])

    confirm_password = PasswordField('Potvrda lozinke',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message="Lozinke se moraju podudarati.")])

    submit = SubmitField('Registruj se')

    def validate_email_custom(self):
        from competition import User

        if not self.email.data.endswith(current_app.config.get('REQUIRED_MAIL_SERVICE')):
            raise ValidationError('Morate se prijaviti sa fakultetskom email adresom')

        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Korisnik sa ovom email adresom već postoji')

    def validate_study_year_custom(self):
        if not self.study_year.data in range(1,5):
            raise ValidationError('Pogrešno unesena godina studija')

    def validate(self):
        """ Method overriding base validation to include additional checks """

        self.validate_email_custom()
        self.validate_study_year_custom()
        return super(RegistrationForm, self).validate()

    def create_student(self):
        from competition import Student
        s = Student(
            name=self.name.data,
            surname=self.surname.data,
            index_number=self.index.data,
            study_year=self.study_year.data,
            email=self.email.data
        )

        s.password = self.password.data
        return s