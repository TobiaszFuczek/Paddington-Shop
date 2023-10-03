from model.service.basket_service import BasketService
from view.view import View


class BasketController:
    def __init__(self):
        self.view = View()
        self.basket_service = BasketService()

    
