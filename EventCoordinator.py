__author__ = 'greg'


class EventCoordinator():
    __slots__ = ("listeners")

    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)
        print("Current Subscription Count: %d" % len(self.listeners))

    def unregister(self, listener):
        self.listeners.remove(listener)
        print("Current Subscription Count: %d" % len(self.listeners))

    def accept(self, event):
        for listener in self.listeners:
            listener.accept(event)


COORDINATOR = EventCoordinator()
