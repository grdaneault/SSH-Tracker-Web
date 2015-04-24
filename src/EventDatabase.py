import mysql.connector
import ipaddress

from src.settings import DATABASE
from src.EventCoordinator import COORDINATOR

class EventDatabase():

    INSERT_4_HOST = "INSERT INTO host (ip4, hostname, country_code, subdivision, city, latitude, longitude) VALUES (inet_aton('%s'), '%s', '%s', '%s', '%s', %d, %d)"
    INSERT_6_HOST = "INSERT INTO host (ip6, hostname, country_code, subdivision, city, latitude, longitude) VALUES (inet6_aton('%s'), '%s', '%s', '%s', '%s', %d, %d)"
    CHECK_4_HOST = "SELECT id FROM host WHERE ip4 = inet_aton('%s') AND country = '%s' AND subdivision = '%s' AND city = '%s' AND latitude = %d AND longitude = %d LIMIT 1"
    CHECK_6_HOST = "SELECT id FROM host WHERE ip6 = inet6_aton('%s') AND country = '%s' AND subdivision = '%s' AND city = '%s' AND latitude = %d AND longitude = %d LIMIT 1"
    INSERT_ATTEMPT = "INSERT INTO attempt (date, username, password, clientversion, target, attacker) VALUES (NOW(), '%s', '%s', '%s', %d, %d)"

    def __init__(self):
        self.cnx = mysql.connector.Connect(**DATABASE)


    def get_host_id(self, host):
        addr = ipaddress.ip_address(host.ip)
        cursor = self.cnx.cursor()
        query = EventDatabase.CHECK_4_HOST
        if addr.version() == 6:
            query = EventDatabase.CHECK_6_HOST

        cursor.execute(query, (host.ip, host.hostname, host.country, host.subdivision, host.city, host.latitude, host.longitude))
        for (id) in cursor:
            return id

        cursor.close()
        return None

    def add_host(self, host):
        addr = ipaddress.ip_address(host.ip)
        cursor = self.cnx.cursor()
        query = EventDatabase.INSERT_4_HOST
        if addr.version() == 6:
            query = EventDatabase.INSERT_6_HOST

        cursor.execute(query, (host.ip, host.hostname, host.country, host.subdivision, host.city, host.latitude, host.longitude))
        id = cursor.lastrowid
        cursor.close()
        return id

    def get_or_create_host_id(self, host):
        host = self.get_host_id(host)
        if host is None:
            host = self.add_host(host)

        return host


    def accept(self, event):
        attacker = self.get_or_create_host_id(event.attacker)
        target = self.get_or_create_host_id(event.target)

        cursor = self.cnx.cursor()
        cursor.execute(EventDatabase.INSERT_ATTEMPT, (event.username, event.password, event.clientversion, target, attacker))

COORDINATOR.register(EventDatabase())






