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
