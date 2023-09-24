class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def modify_product_quantity(self, product, quantity):
        # Zmiana ilości produktu w koszyku
        # Jeśli quantity wynosi 0, produkt zostanie usunięty z koszyka
        pass

    def get_total_price(self):
        # Obliczenie łącznej ceny produktów w koszyku
        pass
