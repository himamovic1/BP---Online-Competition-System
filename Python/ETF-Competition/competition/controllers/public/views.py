from flask import render_template

from competition import db
from competition.models.testModel import test


class Public:
    def index(self):
        return render_template('index.html')

    def home(self):
        return render_template('home.html')

    def addNew(self, name):
        a = test(name)

        db.session.add(a)
        db.session.commit()