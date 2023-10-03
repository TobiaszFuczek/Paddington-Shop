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


