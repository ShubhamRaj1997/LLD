from enum import Enum


class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    BIKE = 3
    CYCLE = 4

class VehicleStatus(Enum):
    AVAILABLE = 1
    DAMAGED = 2
    RESERVED = 3
