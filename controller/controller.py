from model.service.auth_service import AuthService
from model.storage.basket_storage import BasketStorage
from model.storage.user_storage import UserStorage
from view.view import View



class Controller:
    def __init__(self):
        self.view = View()
        self.user_storage = UserStorage()
        self.basket_storage = BasketStorage()
        self.auth_service = AuthService()

    def panel_menu(self):
        while True:
            login = self.view.get_str("Please enter your Login: ")
            password = self.view.get_str("Please enter your Password: ")

            user = self.user_storage.find_by_login(login)
            if user and user.password == password:
                user_type = user.user_type  # Pobieramy typ użytkownika
                if user_type == "owner":
                    self.owner_menu()
                elif user_type == "personnel":
                    self.personnel_menu()
                elif user_type == "user":
                    self.user_menu()
                break
            else:
                self.view.print_msg("Login failed. Please check your credentials.")
    def owner_menu(self):
        # Obsługa panelu dla właściciela
        pass

    def personnel_menu(self):
        # Obsługa panelu dla personelu
        pass

    def user_menu(self):
        # Obsługa panelu dla klienta
        pass

    def control(self):
        self.panel_menu()


