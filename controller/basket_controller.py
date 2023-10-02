from model.service.basket_service import BasketService
from view.view import View


class BasketController:
    def __init__(self):
        self.view = View()
        self.basket_service = BasketService()

    def create_product(self):
        # Dodawanie nowego produktu do magazynu
        product_name = self.view.get_input("Enter the product name to add to storage: ")
        product_quantity = int(self.view.get_input("Enter the quantity of the product to add: "))
        self.user_access.add_product_to_storage(product_name, product_quantity)
        self.view.print_message(f"{product_quantity} {product_name}(s) added to storage.")