from abc import ABC, abstractmethod


class DepositSlot(ABC):

    @abstractmethod
    def get_total_amount(self) -> float:
        pass


class CashDepositSlot(DepositSlot):
    def deposit_cash(self, cash):
        pass

    def get_total_amount(self) -> float:
        pass


class CheckDepositSlot(DepositSlot):
    def deposit_chek(self, cash):
        pass

    def get_total_amount(self) -> float:
        pass
