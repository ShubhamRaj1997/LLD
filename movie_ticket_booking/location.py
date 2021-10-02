from movie_ticket_booking.city import City


class Location(object):
    def __init__(self, lat, longt, address, city: City):
        self.lat = lat
        self.longitude = longt
        self.city = city
        self.address = address
