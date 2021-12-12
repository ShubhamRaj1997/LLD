from enum import Enum


class ReservationStatus(Enum):
    INITIATED = 0
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    WAITING = 4
