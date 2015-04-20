
import tornado.ioloop
import tornado.web

from src.AddEventHandler import AddEventHandler
from src.EventSocket import EventSocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/templates/index.html", title="Real-Time Attack Map")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/events", EventSocket),
    (r"/add", AddEventHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": r"C:\Dev\SSH-Tracker-Web\src\static"})
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()