from model.login import Login
from model.model_storage import ModelStorage
from view.view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model_storage = ModelStorage()
        self.login = Login()

    def panel_menu(self):
        while True:
            self.view.print_msg(
                "You are logged in" if self.login.validate_login(self.view.get_str("Please enter your Login: "),
                                                                 self.view.get_str("Please enter your Password: "))
                else "Login failed. Please check your credentials.")

    def control(self):
        self.panel_menu()
