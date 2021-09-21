from abc import ABC, abstractmethod

from models.payer_data import PaymentData, UPIPaymentData, WalletPaymentData


class PaymentService(ABC):
    @abstractmethod
    def initiate_txn(self, amount: float) -> str:
        pass

    @abstractmethod
    def is_txn_completed(self, txn_id: str) -> bool:
        pass

    @abstractmethod
    def make_payment(self, payment_data: PaymentData) -> bool:
        pass


class UPIPaymentService(PaymentService):
    def __init__(self, payment_data: PaymentData):
        self.payment_data = payment_data

    @abstractmethod
    def initiate_txn(self, amount: float) -> str:
        pass

    @abstractmethod
    def is_txn_completed(self, txn_id: str) -> bool:
        pass

    @abstractmethod
    def make_payment(self, upi_payment_data: UPIPaymentData)-> bool:
        pass


class WalletPaymentService(PaymentService):
    def __init__(self, payment_data: PaymentData):
        self.payment_data = payment_data

    @abstractmethod
    def initiate_txn(self, amount: float) -> str:
        pass

    @abstractmethod
    def is_txn_completed(self, txn_id: str) -> bool:
        pass

    @abstractmethod
    def make_payment(self, wallet_payment_data: WalletPaymentData)-> bool:
        pass
