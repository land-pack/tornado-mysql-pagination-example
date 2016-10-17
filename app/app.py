from tornado import web
from tornado import ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("<h1>Hello Landpack</h1>")


if __name__ == '__main__':
    application = web.Application([
            (r'/', IndexHandler),
        ],
        debug=True)
    application.listen(9099)
    ioloop.IOLoop.current().start()
