from hotel_management.enums.enum import RoomType, RoomState


class Room(object):
    def __init__(self, room_number: int, room_type: RoomType, room_state: RoomState, booking_price: float,
                 is_dnd: bool = False, amenities=None):
        self.room_number = room_number
        self.room_type = room_type
        self.room_state = room_state
        self.booking_price = booking_price
        self.is_dnd = is_dnd
        self.amenities = amenities

    def add_amenities(self, amenity):
        self.amenities.add(amenity)

    def checkin(self):
        pass

    def checkout(self):
        pass
