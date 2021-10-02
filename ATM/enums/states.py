from enum import Enum


class TxnStatus(Enum):
    SUCCESS = 0
    PARTIAL_SUCCESS = 2
    FAILURE = 3
    BLOCKED = 4


class CustomerStatus(Enum):
    ACTIVE = 0
    BLOCKED = 2
    BANNED = 3
    COMPROMISED = 4
    INACTIVE = 5


