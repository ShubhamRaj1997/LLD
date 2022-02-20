import itertools
from abc import ABC, abstractmethod

from splitwise.model.expanse_meta import ExpanseMeta
from splitwise.model.split import PercentSplit
from splitwise.model.user import User


class Expense(ABC):
    itr = itertools.count()

    def __init__(self, amount: float, paid_by: User, splits: list, expense_metadata: ExpanseMeta):
        self._id = next(self.itr)
        self.__amount = amount
        self.__paid_by = paid_by
        self.__splits = splits
        self.__expense_metadata = expense_metadata

    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def calculate(self):
        pass

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def paid_by(self):
        return self.__paid_by

    @paid_by.setter
    def paid_by(self, value):
        self.__paid_by = value

    @property
    def splits(self):
        return self.__splits

    @splits.setter
    def splits(self, value):
        self.__splits = value


class EqualExpense(Expense):
    """
    here no need to validate, thus it is a violation of Liskov Principle, better to create a separate class for each
    User here strategy pattern to create two new classes like Expense and AdvanceExpense  and then inherit
    EqualExpense from Expense and others who need to validate the data can be inherited from AdvanceExpense
    """

    def calculate(self):
        total_splits = len(self.splits)
        split_amount = self.amount/total_splits
        for split in self.splits:
            split.amount = split_amount
        self.splits[0].amount = self.amount - (total_splits-1)*split_amount



    def validate(self) -> bool:
        pass

    def __init__(self, amount: float, paid_by: User, splits: list, expense_metadata: ExpanseMeta):
        super().__init__(amount, paid_by, splits, expense_metadata)


class ExactExpense(Expense):
    def calculate(self):
        pass

    def validate(self) -> bool:
        pass

    def __init__(self, amount: float, paid_by: User, splits: list, expense_metadata: ExpanseMeta):
        super().__init__(amount, paid_by, splits, expense_metadata)


class PercentExpense(Expense):
    def calculate(self):
        pass



    def validate(self) -> bool:
        pass

    def __init__(self, amount: float, paid_by: User, splits: list, expense_metadata: ExpanseMeta):
        super().__init__(amount, paid_by, splits, expense_metadata)




