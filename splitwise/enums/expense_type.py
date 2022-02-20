from enum import Enum


class ExpenseType(Enum):
    EQUAL = 0
    EXACT = 1
    PERCENT = 2
    