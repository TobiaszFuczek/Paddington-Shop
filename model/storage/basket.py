import uuid

class Basket:
    def __init__(self, products, order_number):
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
        for p in self.products:
            if p['product_id'] == product['product_id']:
                p['quantity'] = quantity
                break

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product['price'] * product['quantity']
        return total_price
