"""
Class allow to make changes in CoffeeShop class
"""
from Coffee_Shop import CoffeeShop


class StorageController:
    """
            Class that help to work with storage of Coffee Shop
            __________

            Attributes
            __________
            shop: CoffeeShop
                Coffee Shop object

            storage: list
                Storage of Coffee Shop

            sold: list
                Sold products of Coffee Shop

            __________

            Methods
            __________
            find_product(self, name: str)
                Return product from storage by name

            format_str(self, arr: list)
                Return formatted string with list of products

            remove_type(self)
                Remove all bakery products from storage

            type_products(self, _type: str)
                Return list of products by type

    """
    def __init__(self, obj: CoffeeShop):
        self.shop = obj
        self.storage = obj.storage
        self.sold = obj.products_sold

    def find_product(self, name: str):
        for item in self.storage:
            if item.name == name.capitalize():
                return item

    def format_str(self, arr: list):
        return "".join(str(item) for item in arr)

    def remove_type(self):
        for item in self.storage:
            if item.type == 'bakery':
                self.storage.remove(item)
                return self.storage

    def type_products(self, _type: str):
        return "".join([str(item) for item in self.storage if item.type in _type])
