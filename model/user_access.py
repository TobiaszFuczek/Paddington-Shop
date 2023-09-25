class UserAccess:
    def __init__(self):
        self.basket = []

    def create_order(self, products_to_add):
        pass


    def add_product_to_basket(self, product):
        self.basket.append(product)

    def remove_product_from_basket(self, product):
        if product in self.basket:
            self.basket.remove(product)

    def modificate_order(self, new_products):
        self.basket = new_products

    def preview_order(self):
        return self.basket

    def remove_order(self):
        return self.basket == []

    def payments(self):
        return payment_method
