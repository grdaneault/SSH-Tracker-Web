from tornado import websocket
from EventCoordinator import COORDINATOR
import json

class EventSocket(websocket.WebSocketHandler):
    def open(self):
        print("Started Websocket")
        COORDINATOR.register(self)
        self.write_message("Welcome")

    def on_message(self, message):
        print("Got data %s" % message);
        self.write_message(message)

    def on_close(self):
        print("Socket closed")
        COORDINATOR.unregister(self)

    def accept(self, event):
        print("Sending event!")
        self.write_message("event: %s" % json.dumps(event))