import datetime
# TODO: correct this using: https://youtu.be/WwNw6WWTX70?t=1066
import uuid

from movie_ticket_booking.cinema_show import CinemaShow
from movie_ticket_booking.enums.booking_status import BookingStatus
from movie_ticket_booking.seat_locker import SeatLocker
from services import PaymentService


class Booking(object):
    def __init__(self, booking_id, show, user_id, seats):
        self.seats = seats
        self.user_id = user_id
        self.show = show
        self.booking_id = booking_id
        self.booking_state = BookingStatus.PAYMENT_PENDING

    def confirm_booking(self):
        self.booking_state = BookingStatus.CONFIRMED

    def cancel_booking(self):
        self.booking_state = BookingStatus.CANCELLED


class BookingHandler(object):
    def __init__(self, seats, status: BookingStatus, show: CinemaShow, user, seat_locker=None):
        self.show = show
        self.status = status
        self.seats = seats
        self.__created_at = datetime.datetime.now()
        self.user = user
        self.__payment_service = None
        self.__bookings = []
        self.__seat_locker = seat_locker

    @property
    def seat_locker(self):
        if not self.__seat_locker:
            self.__seat_locker = SeatLocker()
        return self.__seat_locker

    @seat_locker.setter
    def seat_locker(self, seat_locker):
        self.__seat_locker = seat_locker

    @property
    def payment_service(self):
        return self.__payment_service

    @payment_service.setter
    def payment_service(self, payment_service: PaymentService):
        self.__payment_service = payment_service

    # one can move it out from here since it does not do operation related to booking
    def make_payment(self, booking, amount):
        if booking in self.__bookings:
            raise Exception
        booking_idx = self.__bookings.index(booking)
        if self.user != self.__bookings[booking_idx].user:
            raise Exception
        self.__seat_locker.lock_seats(self.show, self.seats)
        try:
            self.payment_service.initiate_payment(amount)
        except Exception:
            self.__seat_locker.release_seats(self.show, self.seats)
            booking.cancel_booking(self.user)
        else:
            booking.confirm_booking(self.user)

    def create_booking(self, seats):
        if any(self.seat_locker.is_seat_locked(seat_id) for seat_id in seats):
            return Exception
        self.seat_locker.lock_seats(self.show, self.seats, self.user)
        booking_id = uuid.uuid1()
        booking = Booking(booking_id, self.show, self.user, seats)
        self.__bookings.append(booking)
        return booking

    def book_seats(self):
        pass
