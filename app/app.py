import os
from tornado import web
from tornado import ioloop
import forgery_py as fy



def gen_many_data(num=1000):
    for i in range(num):
        name = fy.name.full_name()
        addr = fy.address.street_address()
        language = fy.personal.language()
        yield (i, name, addr, language)

class IndexHandler(web.RequestHandler):
    def get(self):
        data = gen_many_data()
        self.render("index.html", data=data)


if __name__ == '__main__':
    application = web.Application([
            (r'/', IndexHandler),
        ],
        template_path = os.path.join(os.path.dirname(__file__),'templates'),
        static_path = os.path.join(os.path.dirname(__file__),'static'),
        debug=True)
    application.listen(9099)
    ioloop.IOLoop.current().start()
