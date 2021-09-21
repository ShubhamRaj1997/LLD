from abc import ABC, abstractmethod


class PaymentData(ABC):

    @abstractmethod
    def get_sender_data(self):
        pass

    @abstractmethod
    def get_receiver_data(self):
        pass


class UPIPaymentData(PaymentData):
    def __init__(self, amount, sender_detail, receiver_detail):
        self.amount = amount
        self.receiver_detail = receiver_detail
        self.sender_detail = sender_detail

    def get_sender_data(self):
        pass

    def get_receiver_data(self):
        pass


class WalletPaymentData(PaymentData):
    def __init__(self, amount, sender_detail, receiver_detail):
        self.amount = amount
        self.receiver_detail = receiver_detail
        self.sender_detail = sender_detail

    def get_sender_data(self):
        pass

    def get_receiver_data(self):
        pass
