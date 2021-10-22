from sortedcontainers import SortedList

from hotel_management.enums.enum import RoomType, RoomState, ReservationStatus
from hotel_management.models.object_iterator import ObjectCollection
from hotel_management.models.person import Person
from hotel_management.models.reservation import Reservation
from hotel_management.models.search import Search


class DateRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        if isinstance(other, int):
            return self.start <= other <= self.end
        else:
            return self.start == other.start and self.end == other.end

    def __le__(self, other):
        if isinstance(other, int):
            return self.end <= other
        else:
            return self.end <= other.end if self.start == other.start else self.start < other.start

    def __ge__(self, other):
        if isinstance(other, int):
            return self.start >= other
        else:
            return self.end >= other.end if self.start == other.start else self.start > other.start

    def __lt__(self, other):
        if isinstance(other, int):
            return self.end < other
        else:
            return self.end < other.end if self.start == other.start else self.start < other.start

    def __gt__(self, other):
        if isinstance(other, int):
            return self.start > other
        else:
            return self.end > other.end if self.start == other.start else self.start > other.start


class Room(Search):
    def __init__(self, room_number: int, room_type: RoomType, room_state: RoomState, booking_price: float,
                 is_dnd: bool = False):
        self.room_number = room_number
        self.room_type = room_type
        self.room_state = room_state
        self.booking_price = booking_price
        self.is_dnd = is_dnd
        self.amenities = ObjectCollection()
        self.reserved_dates = []
        self.date_reservation_map = dict()

    def add_amenities(self, amenity):
        self.amenities.add_item(amenity)

    def checkin(self):
        pass

    def checkout(self):
        pass

    def reserve_room(self, checkin_date, checkout_date, person: Person):
        # we can have two approaches either save for each date the reservation (new)
        #   or save for the segment of dates
        for chkin, chkout in self.reserved_dates:
            if checkin_date in range(chkin, chkout + 1) or checkout_date in range(chkin, chkout + 1):
                # already booked
                return False
        reservation = Reservation(person, ReservationStatus.PENDING, checkin_date, checkout_date, self.room_number)
        self.reserved_dates.append((checkin_date, checkout_date))
        self.date_reservation_map[(checkin_date, checkout_date)] = reservation

    def get_charge(self):
        cost = 0.0
        for amenity in self.amenities:
            cost += amenity.get_charge()
        return cost

    @staticmethod
    def search_rooms(checkin_date, checkout_date, location: str):
        pass
