from model.storage.product_storage import ProductStorage
class Product:
    def __init__(self):
        self.product_storage = ProductStorage()

    def create_new_product(self, product_id, product_name, price, quantity):
        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }

        self.products.append(new_product)



