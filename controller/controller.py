from model.service.auth_service import AuthService
from model.storage.basket_storage import BasketStorage
from model.storage.user_storage import UserStorage
from view.view import View
from model.user_access import UserAccess



class Controller:
    def __init__(self):
        self.view = View()
        self.user_storage = UserStorage()
        self.basket_storage = BasketStorage()
        self.auth_service = AuthService()

    def panel_menu(self):
        while True:
            login = self.view.get_input("Please enter your Login: ")
            password = self.view.get_input("Please enter your Password: ")

            user = self.user_storage.find_by_login(login)
            if user and user.password == password:
                user_type = user.user_type
                if user_type == "owner":
                    self.owner_menu()
                elif user_type == "personnel":
                    self.personnel_menu()
                elif user_type == "user":
                    self.user_menu()

            else:
                self.view.print_message("Login failed. Please check your credentials.")
    def owner_menu(self):
        # Obsługa panelu dla właściciela
        pass

    def personnel_menu(self):
        # Obsługa panelu dla personelu
        pass

    def user_menu(self):
        user_access = UserAccess()

        while True:
            menu_options = [
                "Create Order",
                "Modify Order",
                "Preview Order",
                "Remove Order",
                "Make Payment",
                "Logout"
            ]

            choice = self.view.get_menu_choice(menu_options)

            if choice == "1":
                user_access.create_order()
                self.view.print_message("Order created successfully.")
            elif choice == "2":
                # Tutaj możesz dodać logikę do modyfikacji zamówienia
                modified_order = []  # Zamiast tego powinna być logika modyfikacji zamówienia
                user_access.modify_order(modified_order)
                self.view.print_message("Order modified successfully.")
            elif choice == "3":
                order_preview = user_access.preview_order()
                self.view.print_message("Order Preview:")
                for product in order_preview:
                    self.view.print_message(product)
            elif choice == "4":
                user_access.remove_order()
                self.view.print_message("Order removed.")
            elif choice == "5":
                user_access.make_payment()
                self.view.print_message("Payment successful. Thank you for your purchase.")
            elif choice == "6":
                break
            else:
                self.view.print_message("Invalid choice. Please select a valid option.")


    def control(self):
        self.panel_menu()


