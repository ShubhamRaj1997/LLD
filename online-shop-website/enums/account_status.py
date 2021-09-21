from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 0
    BLOCKED = 1
    BANNED = 2
    UNKNOWN = 3
