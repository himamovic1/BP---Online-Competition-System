import socket

from competition import create_app


def print_local_ip():
    """ Get servers local IP address so it can be accessed inside this network. """
    spacer = '-' * 50
    local_ip = socket.gethostbyname(socket.gethostname())
    print('{}\nLocal IP address is: {}\n{}'.format(spacer, local_ip, spacer))


if __name__ == '__main__':
    print_local_ip()

    app = create_app('development')
    app.run(host=app.config['SERVER_HOST'])
