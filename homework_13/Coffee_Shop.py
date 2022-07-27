"""
Hillel Coffee Shop
"""
from controller_class import *  # Controller class make iterations with list of imported products.
from exception_class import *   # Exception class for coffee shop.
import csv


class Product:
    """
            Class represent products imported from csv file 'inventory'.
            __________

            Attributes
            __________
            _type: str
                Type of product

            name: str
                Name of product

            price: int
                Price of product

            quantity: int
                Quantity of product
            __________

            Methods
            __________
            __str__(self)
                Return string with information about product.

            __repr__(self)
                Do the same as __str__(self)

    """
    def __init__(self, _type: str, name: str, price: int, quantity: int):
        self.type = _type
        self.name = name.capitalize()
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"""
        {self.type.capitalize()}: {self.name}    
        Price: {self.price} UAH            Quantity: {self.quantity}       
                """

    def __repr__(self):
        return self.__str__()


class CoffeeShop:
    """
            Class represent coffee shop.
            __________

            Attributes
            __________
            name: str
                Name of coffee shop

            storage: list
                List of products imported from csv file 'inventory'

            products_sold: list
                List of products sold

            sales: int
                Total sales of coffee shop

            income: int
                Total income of coffee shop

            product_controller: StorageController
                Controller class make iterations with list of imported products.
            __________

            Methods
            __________

            show_income(self)
                Return total income of coffee shop.

            show_sales(self)
                Return total sales of coffee shop.

            total_price(self)
                Return total price of all products that exists in storage.

            import_data(self)
                Import products from csv file 'inventory'

            add_product(self, name: str, quantity: int)
                Add quantity of product to storage.

            sell_product(self, name: str, quantity: int)
                Sell quantity of product from storage.

            combine_types(self, product1: str, product2: str, new_product: str, quantity: int)
                Combine two products to one new product.

            __str__(self)
                Return string with menu of Coffee Shop.

            __repr__(self)
                Return statistics of Coffee Shop.
    """
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.storage = []
        self.products_sold = []
        self.sales = 0
        self.income = 0
        self.product_controller = StorageController(self)

    @property
    def show_income(self):
        return self.income

    @property
    def show_sales(self):
        return self.sales

    @property
    def total_price(self):
        price = 0
        for item in self.storage:
            price += item.price * item.quantity
        return price

    def import_data(self):
        with open('inventory.csv', 'r') as f:
            reader = csv.reader(f)
            next(f)
            for row in reader:
                quantity = row[3]
                if quantity == "":
                    quantity = 5
                self.storage.append(Product(row[1], row[0], int(row[2]), int(quantity)))
            self.product_controller.remove_type()
            return self.storage

    def add_product(self, name: str, quantity: int):
        product = self.product_controller.find_product(name)
        if product is None:
            raise ProductNotFoundError(name)
        else:
            product.quantity += quantity

    def sell_product(self, name: str, quantity: int):
        product = self.product_controller.find_product(name)
        if product is None:
            raise ProductNotFoundError(name)
        if product.quantity < quantity:
            raise OutOfStockError(name)
        else:
            self.products_sold.append(Product(product.type, product.name, product.price, quantity))
            product.quantity -= quantity
            self.sales += quantity
            self.income += product.price * quantity
            return self.products_sold

    def combine_types(self, product1: str, product2: str, new_product: str, quantity: int):
        product_1 = self.product_controller.find_product(product1)
        product_2 = self.product_controller.find_product(product2)
        if product_1 is None or product_2 is None:
            raise ProductNotFoundError(product1 or product2)
        if product_1.type == product_2.type:
            raise SameTypeError(product1 or product2)
        if product_1.type in ('coffee', 'tea') and product_2.type in 'additional':
            if product_1.quantity <= 0 or product_2.quantity <= 0:
                raise OutOfStockError(product1 or product2)
            price = product_1.price + product_2.price + 15
            self.storage.append(Product(product_1.type, new_product, price, quantity))
            product_1.quantity -= quantity
            product_2.quantity -= quantity
        else:
            raise WrongTypeError(product2)
        return self.storage.sort(key=lambda x: x.type)

    def __str__(self):
        return f"""
                Greetings traveller! Welcome to Coffee Shop {self.name}
                We are happy to introduce you our menu: 
                                            {self.product_controller.format_str(self.storage)}
                Enjoy your stay!
                
                """

    def __repr__(self):
        return f'''
        ______________________________________________________
            Statistic for Coffee Shop {self.name}
            \nAll products list: {self.product_controller.format_str(self.storage)}
            \nCoffee list: {self.product_controller.type_products('coffee')}
            \nTea list: {self.product_controller.type_products('tea')}
            Sales: {self.show_sales or "No sales yet"}
            Income: {self.show_income} UAH
            Total price of products: {self.total_price} UAH
            \nProducts Sold: {self.product_controller.format_str(self.products_sold or "No products sold yet")}
            '''


if __name__ == "__main__":
    shop = CoffeeShop("Hillel")
    shop.import_data()
    shop.combine_types('espresso', 'milk', 'latte', 1)
    shop.sell_product('milk', 2)
    shop.add_product('milk', 9)
    shop.combine_types('black tea', 'milk', 'Royal tea', 1)
    shop.combine_types('doppio', 'milk', 'Cappuccino', 1)
    shop.combine_types('Green tea', 'milk', 'Thai Tea', 1)
    shop.sell_product("espresso", 1)
    shop.sell_product("Royal tea", 1)
    shop.sell_product("Americano with milk", 13)
    shop.sell_product("Cappuccino", 1)
    print(shop, repr(shop))
