import datetime
import itertools

from services import PaymentService

itr = itertools.count()


class Transaction(object):

    def __init__(self, user_id: str, product_id: str, amount: float, payment_service: PaymentService,  timestamp=None):
        self.payment_service = payment_service
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.timestamp = timestamp or datetime.datetime.now()
        self._id = next(itr)

    def make_txn(self, payment_data):
        self.payment_service.make_payment(payment_data)
        # log and everything
        return self._id

# Do DB related operations
