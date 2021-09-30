from enum import Enum


class QuestionStatus(Enum):
    ACTIVE = 0
    DUPLICATED = 1
    CLOSED = 2
    BANNED = 3
    DELETED = 4
