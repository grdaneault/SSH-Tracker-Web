import json

from tornado import websocket

from src.EventCoordinator import COORDINATOR


class EventSocket(websocket.WebSocketHandler):
    def open(self):
        print("Started Websocket")
        COORDINATOR.register(self)

    def on_message(self, message):
        pass

    def on_close(self):
        print("Socket closed")
        COORDINATOR.unregister(self)

    def accept(self, event):
        print("Sending event!")
        self.write_message(event.jsonify())