import logging

from tornado.options import define, options
from tornado.ioloop import IOLoop
from app.main import create_app

app = create_app()

define('address', default='0.0.0.0', help='listen address')
define('port', default=4200, help='listen port', type=int)


def run():
    app.listen(options.port, options.address)
    IOLoop.current().start()


if __name__ == '__main__':
    run()