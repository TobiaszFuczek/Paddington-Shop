import uuid

from model.service.product_service import ProductService
from model.storage.basket import Basket
from model.storage.basket_storage import BasketStorage
from model.storage.product_storage import ProductStorage
from model.storage.product import Product
class BasketService:
    def __init__(self):
        self.basket_storage = BasketStorage()
        self.product_service = ProductService()
        self.basket = []
        self.order_number = 0

    def create_basket(self, products):
        new_basket = Basket()
        for product in products:
            new_basket.add_product(product)
        self.basket_storage.add(new_basket)
        return new_basket

    def find_order_by_number(self, order_number):
        for basket in self.basket_storage.find_all():
            if basket.order_number == order_number:
                return basket
        return None



    def find_by_id(self, basket_id: uuid) -> Basket:
        return self.basket_storage.find_by_id(basket_id)

    def add(self, basket: Basket) -> Basket:
        return self.basket_storage.add(basket)

    def update(self, basket: Basket) -> Basket:
        return self.basket_storage.update(basket)
    
    def add_products(self, basket_id: uuid, self.product: products[]):
        basket = self.find_by_id(basket_id)


    def delete(self, basket_id: uuid) -> Basket:
        return self.basket_storage.delete(basket_id)
