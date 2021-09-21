import itertools
from functools import reduce


class Product(object):
    """
    Class for Product, remember this is not the physical product but it contains required information about a product
    It is just a blue print of some product the actual physical product is called here Item
    """
    itr = itertools.count()

    def __init__(self, name, description, price, item, category, _id=None):
        self._id = _id or next(self.itr)
        self.name = name
        self.price = price
        self.item = item
        self.category = category
        self.description = description
        self.__product_reviews = []

    def add_product_review(self, review_id):
        self.__product_reviews.append(review_id)

    def remove_product_review(self, review_id):
        self.__product_reviews.remove(review_id)

    def get_available_count(self):
        return reduce(lambda x, y: x.quantity + y.quantity, self.item)

    def set_available_count(self, count):
        self.item.quantity = count

    def is_available(self, quantity=1):
        return self.get_available_count() >= quantity
