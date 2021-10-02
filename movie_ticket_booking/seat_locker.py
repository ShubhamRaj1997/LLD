from threading import Lock

from movie_ticket_booking.seat_booker import SeatBooker


class SeatLock(object):
    DEFAULT_TIMEOUT = 60

    def __init__(self, seat, show, user, time_out=None):
        self.user = user
        self.show = show
        self.seat = seat
        self.time_out = time_out or self.DEFAULT_TIMEOUT


class SeatLocker(object):
    def __init__(self):
        self.locked_seats = dict()
        self.__lock = Lock()
        self.seat_booker = SeatBooker()

    def lock_seats(self, show, seats, user):
        if any([self.is_seat_locked(seat_id) or self.seat_booker.is_seat_book(show, seat_id) for seat_id in seats]):
            raise Exception
        with self.__lock:
            for seat in seats:
                self.lock_seat(show, seat, user)
            self.seat_booker.book_seats(show, seats)

        # https://www.geeksforgeeks.org/python-how-to-lock-critical-sections/

    def is_seat_locked(self, seat_id):
        return any([seat == seat_id for show, seat in self.locked_seats.items()])

    def lock_seat(self, show, seat_id, user):
        if show in self.locked_seats:
            self.locked_seats[show].update({seat_id: SeatLock(seat_id, show, user)})
        else:
            self.locked_seats[show] = {seat_id: SeatLock(seat_id, show, user)}

    def release_seats(self, show, seats):
        if any([not self.is_seat_locked(seat_id) for seat_id in seats]):
            raise Exception
        with self.__lock:
            for seat in seats:
                self.locked_seats[show].remove(seat)
