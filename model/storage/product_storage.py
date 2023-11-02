from model.storage.product import Product


class ProductStorage:
    def __init__(self):
        """ProductStorage represents the Shop Inventory"""
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)
