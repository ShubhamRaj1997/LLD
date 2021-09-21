from models.product import Product


class Cart(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.__products=[]

    def add_product(self, product_id):
        """
        Quantity of product is available in products's item attribute whicb is a class that contains individual product
        info
        :param product:
        :return:
        """
        self.__products.append(product_id)

    def clear_cart(self):
        self.__products.clear()

    def remove_product(self, product_id):
        self.__products.remove(product_id)
