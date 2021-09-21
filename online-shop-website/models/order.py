from enums.order_status import OrderStatus


class Order(object):
    def __init__(self, customer_id, item, order_id, txn_id, status: OrderStatus):
        self.customer_id = customer_id
        self.item = item
        self.order_id = order_id
        self.txn_id = txn_id
        self.status = status
