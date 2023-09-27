from model.service.auth_service import AuthService
from model.storage.basket_storage import BasketStorage
from model.storage.user_storage import UserStorage
from view.view import View
from model.user_access import UserAccess
from model.storage.basket import Basket



class Controller:
    def __init__(self):
        self.view = View()
        self.user_storage = UserStorage()
        self.basket_storage = BasketStorage()
        self.auth_service = AuthService()
        self.user_access = UserAccess(self.basket_storage)

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
        while True:
            personnel_options = [
                "Add Product to Storage",
                "Modify Order",
                "Add Payment to Order Offline",
                "Back to Main Menu"
            ]

            choice = self.view.get_menu_choice(personnel_options)

            if choice == "1":
                # Dodawanie nowego produktu do magazynu
                product_name = self.view.get_input("Enter the product name to add to storage: ")
                product_quantity = int(self.view.get_input("Enter the quantity of the product to add: "))
                self.user_access.add_product_to_storage(product_name, product_quantity)
                self.view.print_message(f"{product_quantity} {product_name}(s) added to storage.")

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
                order_number = self.view.get_input("Enter the order number to add offline payment: ")
                order_to_modify = self.user_access.find_order_by_number(order_number)

                if order_to_modify is None:
                    self.view.print_message("Order not found.")
                else:
                    payment_amount = float(self.view.get_input("Enter the payment amount: "))
                    self.user_access.add_offline_payment(order_to_modify, payment_amount)
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
                    product = self.view.get_input("Enter the product name (or 'done' finish to add new products): ")

                    if product.lower() == "done":
                        break

                    products_to_add.append(product)

                new_basket = self.user_access.create_order(products_to_add)  # Przekazujemy produkty do create_order
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
                        # Powrót do menu
                        continue
                    elif preview_order_choice == "2":
                        # Wybór opcji płatności
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





                elif create_order_choice == "2":
                    # Wybór opcji płatności
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
        self.panel_menu()


