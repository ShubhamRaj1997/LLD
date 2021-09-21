from abc import abstractmethod, ABC
from typing import List

from managers import ProductManager
from models.product import Product


class SearchProducts(ABC):
    @abstractmethod
    def search_by_product_name(self, name: str) -> List[Product]:
        pass

    @abstractmethod
    def search_by_category_name(self, name: str) -> List[Product]:
        pass


class Catalog(SearchProducts):
    """
    We store product names and categories in some database, indexed on these two fields as of now
    ProductName and ProductCategory
    """

    def search_by_product_name(self, name: str) -> List[Product]:
        """
        Do a search query on product name
        """
        return ProductManager.get_products({"name": name})

    def search_by_category_name(self, category: str) -> List[Product]:
        return ProductManager.get_products({"category": category})
