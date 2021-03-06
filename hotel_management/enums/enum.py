from enum import Enum


class RoomType(Enum):
    REGULAR = 1
    DELUXE = 2
    FAMILY_SUITE = 3


class RoomState(Enum):
    RESERVED = 1
    UNAVAILABLE = 2
    REPAIR = 3


class AccountType(Enum):
    MEMBER = 1
    GUEST = 2
    MANAGER = 3
    RECEPTIONIST = 4


class ReservationStatus(Enum):
    REQUESTED = 0
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    CHECKED_IN = 4
    CHECKED_OUT = 5
