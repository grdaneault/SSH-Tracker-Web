import json


class Event():
    # __slots__ = ("username", "password", "target", "attacker")

    def __init__(self, username, password, target, attacker):
        self.username = username
        self.password = password
        self.target = target
        self.attacker = attacker

    def jsonify(self):
        me = {}
        for f in self.__dict__:
            if f in ["target", "attacker"]:
                me[f] = self.__dict__[f].__dict__
            else:
                me[f] = self.__dict__[f]

        return json.dumps(me)


class Host():
    # __slots__ = ("ip", "hostname", "country", "subdivision", "city", "longitude", "latitude")

    def __init__(self, ip, hostname, country = "", subdivision = "", city = "", longitude = 0, latitude = 0):
        self.ip = ip
        self.hostname = hostname
        self.country = country
        self.subdivision = subdivision
        self.city = city
        self.longitude = longitude
        self.latitude = latitude