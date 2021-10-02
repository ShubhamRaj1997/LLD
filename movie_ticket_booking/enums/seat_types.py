from enum import Enum


class SeatTypes(Enum):
    REGULAR = 0
    PREMIUM = 1
    BALCONY = 2
    EMERGENCY = 3
    ACCESSIBLE = 4


class SeatState(Enum):
    OCCUPIED = 0
    EMPTY = 1
