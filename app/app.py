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

def gen_page(num=1000, page=10):
    a = []
    for j in range(0,num,page):
        d = gen_many_data(page)
        a.append(d)
    return a



class IndexHandler(web.RequestHandler):
    def get(self):

        data = gen_many_data()
        self.render("index.html", data=data)

class PaginationHandler(web.RequestHandler):
    def get(self):
        page = self.get_argument('page')
        data = gen_page(1000)
        page = int(page)
        page_data = data[page]
        max_page = 100
        self.render('page.html', data=page_data, page=page, max=max_page)        

if __name__ == '__main__':
    application = web.Application([
            (r'/', IndexHandler),
            (r'/page', PaginationHandler),
        ],
        template_path = os.path.join(os.path.dirname(__file__),'templates'),
        static_path = os.path.join(os.path.dirname(__file__),'static'),
        debug=True)
    application.listen(9099)
    ioloop.IOLoop.current().start()
