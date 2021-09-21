from functools import reduce


class Product(object):
    """
    Class for Product, remember this is not the physical product but it contains required information about a product
    It is just a blue print of some product the actual physical product is called here Item
    """
    def __init__(self, name, description, price, item, category):
        self.name = name
        self.price = price
        self.item = item
        self.category = category
        self.description = description

    def get_available_count(self):
        return reduce(lambda x, y: x.quantity + y.quantity, self.item)

    def set_available_count(self, count):
        self.item.quantity = count
