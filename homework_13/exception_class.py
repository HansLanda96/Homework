"""
Coffee Shop exceptions
"""


class MyException(Exception):
    """Class for creating exceptions"""
    pass


class OutOfStockError(MyException):
    """Exception for out of stock"""
    def __init__(self, name: str):
        self.message = 'Product(s) is out of stock. Use add_product method to add products from inventory'
        self.name = name.capitalize()

    def __str__(self):
        return f'{self.name} -> {self.message}'


class WrongTypeError(MyException):
    """Exception for wrong type"""
    def __init__(self, name: str):
        self.message = "Product is not an Additional type"
        self.name = name.capitalize()
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} -> {self.message}'


class SameTypeError(MyException):
    """Exception for same type"""
    def __init__(self, name: str):
        self.message = "Products are of the same type"
        self.name = name.capitalize()
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} -> {self.message}'


class ProductNotFoundError(MyException):
    """Exception for product not found"""
    def __init__(self, name: str):
        self.message = 'Product is not found in storage'
        self.name = name.capitalize()
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} -> {self.message}'
