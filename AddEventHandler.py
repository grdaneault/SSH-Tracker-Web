import tornado.web
import json
from EventCoordinator import COORDINATOR

class AddEventHandler(tornado.web.RequestHandler):

    def post(self):
        event = self.get_argument("event", "")
        event = json.loads(event)
        print(event)
        COORDINATOR.accept(event)
