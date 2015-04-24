
import random
import json
from geoip2.errors import AddressNotFoundError

import tornado.web
import geoip2.database

from src.EventCoordinator import COORDINATOR
from src.Event import Event, Host

class AddEventHandler(tornado.web.RequestHandler):

    def post(self):
        event = self.get_argument("event", "")
        event = json.loads(event)
        target = Host(self.request.remote_ip, self.request.remote_ip)
        try:
            reader = geoip2.database.Reader("GeoLite2-City.mmdb")
            response = reader.city(self.request.remote_ip)
            country = response.country.name
            subdivision = response.subdivisions.most_specific.name
            city = response.city.name
            lat = response.location.latitude
            lon = response.location.longitude
            target = Host(self.request.remote_ip, self.request.remote_ip, country, subdivision, city, lon, lat)
        except AddressNotFoundError:
            target = Host(self.request.remote_ip, self.request.remote_ip, "", "", "", -77.63, 43.09)
            print("No location data for %s." % self.request.remote_ip)

        if event.get("longitude", 0) == 0 and event.get("latitude", 0) == 0:
            del event["longitude"]
            del event["latitude"]

        attacker = Host(event.get("ip", "IP Missing"),
                        event.get("hostname", "Hostname Missing"),
                        event.get("country", ""),
                        event.get("subdivision", ""),
                        event.get("city", ""),
                        event.get("longitude", random.randrange(-100, 100)),
                        event.get("latitude", random.randrange(-100, 100)))
        attempt = Event(event["username"], event["password"], event["clientVersion"], target, attacker)
        print(event)
        COORDINATOR.accept(attempt)
