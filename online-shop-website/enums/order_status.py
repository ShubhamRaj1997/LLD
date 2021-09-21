from enum import Enum


class OrderStatus(Enum):
    INITIATED = 0
    PENDING = 1
    PAID = 2
    UNSHIPPED = 3
    SHIPPED = 4
    COMPLAINED = 5
    COMPLETED = 6
