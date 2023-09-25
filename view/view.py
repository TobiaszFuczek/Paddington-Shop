class View:
    def print_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)

    def display_menu(self, menu_options):
        for index, option in enumerate(menu_options, start=1):
            print(f"{index}. {option}")

    def get_menu_choice(self, menu_options):
        self.display_menu(menu_options)
        choice = self.get_input("Please select an option: ")
        return choice