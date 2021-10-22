from datetime import datetime

from hotel_management.enums.enum import ReservationStatus
from hotel_management.models.person import Person


class Reservation(object):
    def __init__(self, person:Person, status:ReservationStatus, checkin:datetime, checkout:datetime, room):
        self.person = person
        self.status = status
        self.checkin = checkin
        self.checkout = checkout
        self.room = room
