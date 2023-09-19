class View:
    def print_msg(self,msg):
        print(msg)

    def get_str(self, msg):
        self.print_msg(msg)
        return input()

class Model:
    def __init__(self, name):
        self.name = name

class ModelStorage:

    def __init__(self):
        self.storage = []

    def append(self, model):
        self.storage.append(model)

class Controller:
    def __init__(self):
        self.view = View()
        self.model_storage = ModelStorage()

    def panel_menu(self):
        while True:
            username = self.view.get_str("Please enter your Login: ")
            password = self.view.get_str("Please enter your Password: ")

            if self.Login().validate_login(username, password):
                self.view.print_msg("You are logged in")
                break
            else:
                self.view.print_msg("Login failed. Please check your credentials.")
    class Login:
        def __init__(self):
            self.users = {
                "owner": "owner_password",
                "personnel": "personnel_password",
                "user": "user_password",
            }

        def validate_login(self, username, password):
            if username in self.users and self.users[username] == password:
                return True
            else:
                return False

    def control(self):
        self.panel_menu()

class UserAccess:
    def __init__(self):
        self.basket = []

    def add_product_to_basket(self, product):
        self.basket.append(product)

    def modificate_order(self, new_products):
        self.basket = new_products

    def preview_order(self):
        return self.basket

    def remove_order(self):
        return self.basket == []

    def payments(self):
        return payment_method



if __name__=="__main__":
    Controller().control()

