from model.storage.product import Product


class ProductStorage:
    def __init__(self):
        """ProductStorage represents the Shop Inventory"""
        '''
        self.products = []
        
        '''
        """Testing list"""
        self.products = [10011, 10012, 10013, 10014, 10015]
    def add(self, product: Product) -> None:
        self.products.append(product)
