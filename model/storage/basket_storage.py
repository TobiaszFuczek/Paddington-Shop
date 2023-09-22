import uuid

from model.storage.basket import Basket


class BasketStorage:
    def __init__(self):
        pass

    def find_all(self) -> list:
        pass

    def find_by_id(self, basket_id: uuid) -> Basket:
        pass

    # Once adding the new Basket the id should not be populated
    def add(self, basket: Basket) -> Basket:
        pass

    # Once adding the new Basket the id should be populated
    def update(self, basket: Basket) -> Basket:
        pass

    def delete(self, basket_id: uuid) -> Basket:
        pass
