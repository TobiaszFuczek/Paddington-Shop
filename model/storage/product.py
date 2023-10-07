from model.storage.product_storage import ProductStorage

class Product:
    def __init__(self, product_storage):
        self.product_storage = product_storage

    def create_new_product(self, product_id, product_name, price, quantity):
        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }

        self.product_storage.products.append(new_product)



