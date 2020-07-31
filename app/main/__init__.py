import uuid
import tornado.web

from .worker import Worker
from .handlers import main_handler


def create_app():
    settings = {
        'cookie_secret': uuid.uuid1().hex,
        'xsrf_cookies': False,
        'debug': True
    }

    app_handlers = [
        (r'/',   main_handler.MainHandler),
        (r'/ws', main_handler.WsHandler)
    ]

    app = tornado.web.Application(app_handlers, **settings)

    return app




