import uuid

from model.storage.basket import Basket


class BasketStorage:
    def __init__(self):
        self.baskets = {}

    def find_all(self) -> list:
        return list(self.baskets.values())

    def find_by_id(self, basket_id: uuid) -> Basket:
        return self.baskets.get(basket_id)

    # Once adding the new Basket the id should not be populated
    def add(self, basket: Basket) -> Basket:
        basket_id = uuid.uuid4()
        basket.id = basket_id
        basket.order_number = str(uuid.uuid4())  # Unikalny numer zamówienia
        self.baskets[basket_id] = basket
        return basket

    # Once adding the new Basket the id should be populated
    def update(self, basket: Basket) -> Basket:
        self.baskets[basket.id] = basket
        return basket

    def delete(self, basket_id: uuid) -> Basket:
        return self.baskets.pop(basket_id, None)
