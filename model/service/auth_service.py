from model.storage.user_storage import UserStorage


class AuthService:
    def __init__(self):
        self.user_storage = UserStorage()

    def authenticate(self, login: str, password: str):
        # db_user = self.user_storage.find_by_login(user.login)
        # return db_user.login == login and db_user.password == password
        pass
