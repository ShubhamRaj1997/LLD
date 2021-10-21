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

