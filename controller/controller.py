from model.storage.basket_storage import BasketStorage
from model.storage.user_storage import UserStorage
from view.view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.user_storage = UserStorage()
        self.basket_storage = BasketStorage()

    def panel_menu(self):
        while True:
            self.view.print_msg(
                "You are logged in" if self.login.validate_login(self.view.get_str("Please enter your Login: "),
                                                                 self.view.get_str("Please enter your Password: "))
                else "Login failed. Please check your credentials.")

    def control(self):
        self.panel_menu()
