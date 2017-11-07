from flask import render_template

from competition import db, Competition
from competition.models.Field import Field


class Public:
    def index(self):
        return render_template('index.html')

    def home(self):
        return render_template('home.html')

    # it works
    def create_field(self, name):
        newField = Field(name)

        db.session.add(newField)
        db.session.commit()
