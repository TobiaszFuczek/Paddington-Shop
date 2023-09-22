class View:
    def print_msg(self, msg):
        print(msg)

    def get_str(self, msg):
        self.print_msg(msg)
        return input()
