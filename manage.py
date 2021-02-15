from tornado.options import define, options
from tornado.ioloop import IOLoop
from app.main import create_app

define('port', default=8000, help='listen port', type=int)

app = create_app()


def main():
    app.listen(options.port)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
