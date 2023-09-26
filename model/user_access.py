from model.storage.basket import Basket
class UserAccess:
    def __init__(self, basket_storage):
        self.basket = []
        self.basket_storage = basket_storage
        self.order_number = 0

    def create_order(self, products):
        new_basket = Basket()
        for product in products:
            new_basket.add_product(product)
        self.basket_storage.add(new_basket)  # Dodaj koszyk do magazynu koszyków
        return new_basket

    def find_order_by_number(self, order_number):
        for basket in self.basket_storage.find_all():
            if basket.order_number == order_number:
                return basket
        return None  # Zwracaj None, jeśli nie znaleziono zamówienia

    def add_product_to_basket(self, basket, product):
        basket.add_product(product)

    def remove_product_from_basket(self, basket, product):
        basket.remove_product(product)

    def modificate_order(self, new_products):
        self.basket = new_products

    def preview_order(self, order):
        return order.get_products()

    def get_order_list(self):
        return self.basket_storage.find_all()

    def remove_order(self, basket):
        if basket:
            self.basket_storage.delete(basket.id)

    def payments(self):
        return payment_method
