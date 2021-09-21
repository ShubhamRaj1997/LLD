import itertools

from enums.account_status import AccountStatus
from exceptions import ProductNotFoundException
from models.Address import Address
from models.cart import Cart
from models.payer_data import PaymentData
from models.product import Product
from models.product_review import ProductReview
from models.transaction import Transaction
from services import PaymentService


class Account(object):
    def __init__(self, status: AccountStatus, name: str, address: Address, phone: str, email: str):
        self.status = status
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


# separate out buyer and seller , although Seller could have inherited all the methods of buyer as well
# since it can be  a buyer as well, but let us stick to different acoounts, otherwise each seller account will have
# to implement the methods and there won't be different customer id, which in turn create problems whenever we want
# to handle them independently of each other, like seller will receive some internal notifications from company
# related to GST data or stats, but your customer don't need to be there

class Buyer(object):
    itr = itertools.count()

    def __init__(self, _id, account):
        self._id = next(self.itr)
        self.account_info = account
        self.__reviews =[]

    def place_order(self, user_id: str, product: Product, quantity:int, payment_data: PaymentData, payment_service:PaymentService):
        # fetch the product from product_id in real case, for simplicity
        # get the cost and quantity of product
        if not product.is_available(quantity):
            raise ProductNotFoundException()
        txn = Transaction(user_id, product._id, product.price, payment_service)
        txn_id = txn.make_txn(payment_data)
        product.set_available_count(product.get_available_count()-quantity)

    def add_to_cart(self, product):
        cart = Cart(self._id)
        cart.add_product(product.id)

    def add_review(self, title, message, product_id, rating):
        pr = ProductReview(product_id, self._id, title, rating, message )
        self.__reviews.append(pr.id)



class Seller(object):
    pass
    # seller_id
    # add product
    # remove product
    # block buyer
    # modify product
    pass
