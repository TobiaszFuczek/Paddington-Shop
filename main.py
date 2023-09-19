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
        return self.basket = []

    def payments(self):
        return payment_method



if __name__=="__main__":
