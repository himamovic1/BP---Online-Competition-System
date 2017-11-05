from flask import render_template


class Public:
    def index(self):
        return render_template('index.html')

    def home(self):
        return render_template('home.html')
