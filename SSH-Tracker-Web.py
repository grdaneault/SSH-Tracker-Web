import tornado.ioloop
import tornado.web
from AddEventHandler import AddEventHandler
from EventSocket import EventSocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html", title="Real-Time Attack Map")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/events", EventSocket),
    (r"/add", AddEventHandler)
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()