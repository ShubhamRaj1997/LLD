class Hotel(object):
    def __init__(self, name):
        self.name = name
        self.hotel_locations = []


class HotelLocation(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []

    def add_rooms(self, rooms):
        self.rooms.extend(rooms)

    def get_rooms(self):
        return self.rooms
