from controller.user_controller import UserController
from model.storage.basket_storage import BasketStorage
from view.view import View
from model.storage.product import Product
from model.service.product_service import ProductService
from model.storage.product_storage import ProductStorage
from model.service.basket_service import BasketService

class Controller:
    def __init__(self):

        self.basket_service = BasketService()
        self.view = View()
        self.user_controller = UserController()
        self.basket_storage = BasketStorage()
        self.product_storage = ProductStorage()
        self.product = Product(self.product_storage)
        self.product_service = ProductService()

    def start(self):
        while True:
            role = self.user_controller.authenticate_action()
            if role:
                self.menu_action(role)
            else:
                self.view.print_message("Login failed. Please check your credentials.")

    def menu_action(self, role):
        if role == "owner":
            self.owner_menu()
        elif role == "personnel":
            self.personnel_menu()
        elif role == "user":
            self.user_menu()

    def owner_menu(self):
        # Obsługa panelu dla właściciela
        pass

    def personnel_menu(self):
        while True:
            personnel_options = [
                "Add Product to Storage",
                "Modify Order",
                "Add Payment to Order Offline",
                "Back to Main Menu"
            ]

            choice = self.view.get_menu_choice(personnel_options)

            if choice == "1":
                while True:
                    product_id = self.view.get_input("Enter Product ID (5 numbers): ")
                    valid_product_id = self.product_service.validate_product_id(product_id)
                    if valid_product_id:
                        break
                    else:
                        print("Invalid Product ID format. Please enter 5 numbers.")


                product_name = self.view.get_input("Enter Product Name: ")
                while True:
                    price_input = self.view.get_input("Enter Price in Format xx.xx: ")
                    price = self.product_service.validate_price(price_input)
                    if price is not None:
                        break
                    else:
                        print("Invalid price format. Please enter price in the format xx.xx.")


                quantity_input = float(self.view.get_input("Enter quantity: "))
                self.product.create_new_product(product_id,product_name,price,quantity_input)



            elif choice == "2":
                order_number = self.view.get_input("Enter the order number to modify: ")
                order_to_modify = self.basket_service.find_order_by_number(order_number)

                if order_to_modify is None:
                    self.view.print_message("Order not found.")
                else:
                    while True:
                        modification_options = [
                            "Add Product to Order",
                            "Remove Product from Order",
                            "Finish Modification"
                        ]
                        modification_choice = self.view.get_menu_choice(modification_options)

                        if modification_choice == "1":
                            product = self.view.get_input("Enter the product name to add: ")
                            self.basket_service.add(order_to_modify)
                            self.view.print_message(f"{product} added to the order.")
                        elif modification_choice == "2":
                            self.view.print_message("Products in the order:")
                            for product in order_to_modify.products:
                                self.view.print_message(product)

                            product = self.view.get_input("Enter the product name to remove: ")
                            self.basket_service.remove_product_from_basket(order_to_modify, product)
                            self.view.print_message(f"{product} removed from the order.")
                        elif modification_choice == "3":
                            break
                        else:
                            self.view.print_message("Invalid choice. Please select a valid option.")

                    self.view.print_message("Order modified successfully.")

            elif choice == "3":
                order_number = self.view.get_input("Enter the order number to add offline payment: ")
                order_to_modify = self.basket_service.find_order_by_number(order_number)

                if order_to_modify is None:
                    self.view.print_message("Order not found.")
                else:
                    self.view.print_message("Offline payment added to the order.")

            elif choice == "4":
                break
            else:
                self.view.print_message("Invalid choice. Please select a valid option.")

    def user_menu(self):
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
                products_to_add = []
                while True:
                    self.view.print_message(self.product_storage.products)
                    product = self.view.get_input("Enter the product name (or 'done' finish to add new products): ")


                    if product.lower() == "done":
                        break

                    products_to_add.append(product)

                new_basket = self.basket_service.create_basket(self.products)
                self.view.print_message(f"Order created successfully. Order number: {new_basket.order_number}")

                create_order_options = [
                    "Preview Order",
                    "Make Payment"
                ]
                create_order_choice = self.view.get_menu_choice(create_order_options)

                if create_order_choice == "1":
                    # Podgląd zamówienia
                    order_preview = new_basket.get_products()
                    self.view.print_message("Order Preview:")
                    for product in order_preview:
                        self.view.print_message(product)

                    preview_order_options = [
                        "Return to Menu",
                        "Proceed to Payment"
                    ]
                    preview_order_choice = self.view.get_menu_choice(preview_order_options)

                    if preview_order_choice == "1":
                        continue
                    elif preview_order_choice == "2":
                        payment_options = [
                            "Online Payment (Credit Card)",
                            "Online Payment (PayPal)",
                            "Offline Payment (After Product Delivery)"
                        ]
                        payment_choice = self.view.get_menu_choice(payment_options)

                        if payment_choice == "1":
                            self.view.print_message("Online Credit Card Payment Process")
                        elif payment_choice == "2":
                            self.view.print_message("Online PayPal Payment Process")
                        elif payment_choice == "3":
                            self.view.print_message("Offline Payment (After Product Delivery) Process")
                        else:
                            self.view.print_message("Invalid payment choice.")





                elif create_order_choice == "2":
                    payment_options = [
                        "Online Payment (Credit Card)",
                        "Online Payment (PayPal)",
                        "Offline Payment (After Product Delivery)"
                    ]
                    payment_choice = self.view.get_menu_choice(payment_options)

                    if payment_choice == "1":
                        # Implementuj obsługę płatności kartą kredytową
                        self.view.print_message("Online Credit Card Payment Process")
                    elif payment_choice == "2":
                        # Implementuj obsługę płatności PayPal
                        self.view.print_message("Online PayPal Payment Process")
                    elif payment_choice == "3":
                        # Implementuj obsługę płatności offline
                        self.view.print_message("Offline Payment (After Product Delivery) Process")
                    else:
                        self.view.print_message("Invalid payment choice.")

            elif choice == "2":
                order_number = self.view.get_input("Enter the order number to modify: ")
                order_to_modify = self.user_access.find_order_by_number(order_number)

                if order_to_modify is None:
                    self.view.print_message("Order not found.")
                else:
                    while True:
                        modification_options = [
                            "Add Product to Order",
                            "Remove Product from Order",
                            "Finish Modification"
                        ]
                        modification_choice = self.view.get_menu_choice(modification_options)

                        if modification_choice == "1":
                            product = self.view.get_input("Enter the product name to add: ")
                            self.user_access.add_product_to_basket(order_to_modify, product)
                            self.view.print_message(f"{product} added to the order.")
                        elif modification_choice == "2":
                            self.view.print_message("Products in the order:")
                            for product in order_to_modify.products:
                                self.view.print_message(product)

                            product = self.view.get_input("Enter the product name to remove: ")
                            self.user_access.remove_product_from_basket(order_to_modify, product)
                            self.view.print_message(f"{product} removed from the order.")
                        elif modification_choice == "3":
                            break
                        else:
                            self.view.print_message("Invalid choice. Please select a valid option.")

                    self.view.print_message("Order modified successfully.")

            elif choice == "3":
                order_list = self.user_access.get_order_list()
                self.view.print_message("Available Orders:")
                for order in order_list:
                    self.view.print_message(order.order_number)

                selected_order_number = self.view.get_input(
                    "Enter the order number to preview (or 'back' to go back): ")
                if selected_order_number == "back":
                    continue

                selected_order = self.user_access.find_order_by_number(selected_order_number)
                if selected_order:
                    order_preview = selected_order.get_products()
                    self.view.print_message("Order Preview:")
                    for product in order_preview:
                        self.view.print_message(product)
                else:
                    self.view.print_message("Order not found.")
            elif choice == "4":
                order_list = self.user_access.get_order_list()
                self.view.print_message("Available Orders:")
                for order in order_list:
                    self.view.print_message(order.order_number)

                selected_order_number = self.view.get_input("Enter the order number to remove (or 'back' to go back): ")
                if selected_order_number == "back":
                    continue

                selected_order = self.user_access.find_order_by_number(selected_order_number)
                if selected_order:
                    self.user_access.remove_order(selected_order)
                    self.view.print_message(f"Order {selected_order_number} removed.")
                else:
                    self.view.print_message("Order not found.")
            elif choice == "5":
                # Lista dostępnych zamówień do zapłaty
                order_list = self.user_access.get_order_list()
                self.view.print_message("Available Orders to Make Payment:")
                for order in order_list:
                    self.view.print_message(order.order_number)

                # Użytkownik wybiera zamówienie do zapłaty
                selected_order_number = self.view.get_input(
                    "Enter the order number to make payment (or 'back' to go back to the menu): ")

                if selected_order_number == "back":
                    continue

                selected_order = self.user_access.find_order_by_number(selected_order_number)

                if selected_order:
                    # Użytkownik wybiera sposób płatności
                    payment_options = [
                        "Online Payment (Credit Card)",
                        "Online Payment (PayPal)",
                        "Offline Payment (After Product Delivery)"
                    ]
                    payment_choice = self.view.get_menu_choice(payment_options)

                    if payment_choice == "1":
                        # Implementuj obsługę płatności kartą kredytową dla wybranego zamówienia
                        self.view.print_message("Online Credit Card Payment Process")
                    elif payment_choice == "2":
                        # Implementuj obsługę płatności PayPal dla wybranego zamówienia
                        self.view.print_message("Online PayPal Payment Process")
                    elif payment_choice == "3":
                        # Implementuj obsługę płatności offline dla wybranego zamówienia
                        self.view.print_message("Offline Payment (After Product Delivery) Process")
                    else:
                        self.view.print_message("Invalid payment choice.")
                else:
                    self.view.print_message("Order not found.")
            elif choice == "6":
                break
            else:
                self.view.print_message("Invalid choice. Please select a valid option.")

    def control(self):
        self.start()
