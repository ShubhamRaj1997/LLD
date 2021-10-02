from abc import ABC, abstractmethod


class PaymentService(ABC):
    @abstractmethod
    def initiate_payment(self):
        pass

class CashPaymentService(PaymentService):

    def initiate_payment(self):
        pass

class CreditCardPaymentService(PaymentService):
    def initiate_payment(self):
        pass