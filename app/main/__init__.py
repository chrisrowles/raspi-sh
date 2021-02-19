import uuid
import tornado.web

from app.main.handlers import main
from app.main.worker import Worker


def create_app():
    settings = {
        'cookie_secret': uuid.uuid1().hex,
        'xsrf_cookies': False,
        'debug': True
    }

    handlers = [
        (r'/',   main.HttpHandler),
        (r'/ws', main.WebsocketHandler)
    ]

    app = tornado.web.Application(handlers, **settings)

    return app




