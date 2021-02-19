import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        self.write('Silence is golden.')

    def get(self):
        self.write('Silence is golden.')

    def options(self):
        self.set_status(204)
        self.finish()