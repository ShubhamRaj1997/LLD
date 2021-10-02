from enum import Enum


class BookingStatus(Enum):
    ACTIVE = 0
    CANCELLED = 1
    WAITING = 2
    PAYMENT_PENDING =3
    CONFIRMED = 4
