import uuid

class Basket:
    def __init__(self, products=None, order_number=None):
        self.id = uuid.uuid4()
        self.products = products if products is not None else []
        self.order_number = order_number

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

    def modify_product_quantity(self, product, quantity):
        pass

    def get_total_price(self):
        pass
