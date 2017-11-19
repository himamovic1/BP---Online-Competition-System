from competition import create_app, db
from socket import gethostname, gethostbyname


def print_local_ip():
    """ Get servers local IP address so it can be accessed inside this network. """
    spacer = '-' * 50
    local_ip = gethostbyname(gethostname())
    print('\n{}\nLocal IP address is: {}\n{}'.format(spacer, local_ip, spacer))


if __name__ == '__main__':
    print_local_ip()

    app = create_app('development')
    app.run(host=app.config['SERVER_HOST'], debug=app.config['DEBUG'])

    # u = User('John', 0, 'john.doe@gmail.com')
    # u.password = "1DvaTri!"
    # db.session.add(u)
    # db.session.commit()