from flask import Flask

from competition.controllers.auth.views import Auth

app = Flask(__name__)


@app.route('/')
def hello_world():
    auth = Auth()
    auth.get()


if __name__ == '__main__':
    app.run()
