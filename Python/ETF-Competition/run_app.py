from flask import Flask

from competition.controllers.auth.views import Auth
from competition.controllers.public.views import Public

app = Flask(__name__, template_folder='competition/templates')


@app.route('/')
def index():
    public = Public()
    return public.index()


@app.route('/home')
def home():
    public = Public()
    return public.home()


if __name__ == '__main__':

    # Print current local IP address of the server
    import socket
    print('{}\nLocal server IP address: {}\n{}'.format(
        '-' * 50,
        socket.gethostbyname(socket.gethostname()),
        '-' * 50)
    )

    # Run the server
    app.run(host='0.0.0.0')
