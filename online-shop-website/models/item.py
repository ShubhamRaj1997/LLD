import itertools


class Item(object):
    itr = itertools.count()

    def __init__(self, quantity, price, _id=None):
        self.__quantity = quantity
        self.__price = price
        self._id = _id or next(self.itr)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

