import uuid

from model.service.product_service import ProductService
from model.storage.basket import Basket
from model.storage.basket_storage import BasketStorage

class BasketService:
    def __init__(self):
        self.basket_storage = BasketStorage()
        self.product_service = ProductService()

    def find_all(self) -> list:
        return self.basket_storage.find_all()

    def find_by_id(self, basket_id: uuid) -> Basket:
        return self.basket_storage.find_by_id(basket_id)

    def add(self, basket: Basket) -> Basket:
        return self.basket_storage.add(basket)

    def update(self, basket: Basket) -> Basket:
        return self.basket_storage.update(basket)
    
    def add_products(self, basket_id: uuid, products: Product[]):
        basket = self.find_by_id(basket_id)
        if basket:
            
        return 

    def delete(self, basket_id: uuid) -> Basket:
        return self.basket_storage.delete(basket_id)
