from model.service.auth_service import AuthService
from view.view import View


class UserController():
    def __init__(self):
        self.view = View()
        self.auth_service = AuthService()

    def authenticate_action(self):
        return self.auth_service.authenticate(self.view.get_input("Please enter your Login: "),
                                              self.view.get_input("Please enter your Password: "))


