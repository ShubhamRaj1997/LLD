import itertools

from movie_ticket_booking.enums.seat_types import SeatState, SeatTypes


class Seat(object):
    def __init__(self, seat_state: SeatState, seat_type: SeatTypes, price):
        self.__id = next(itertools.count())
        self.seat_type = seat_type
        self.seat_state = seat_state
        self.price = price
