import uuid

from model.storage.user import User


class UserStorage:
    def __init__(self):
        self.users = {
            "owner": User("owner", "owner_password", "owner"),
            "personnel": User("personnel", "personnel_password", "personnel"),
            "user": User("user", "user_password", "user"),
        }

    def find_all(self) -> list:
        pass

    def find_by_id(self, user_id: uuid) -> User:
        pass

    # Once adding the new User the id should not be populated
    def add(self, user: User) -> User:
        pass

    # Once adding the new User the id should be populated
    def update(self, user: User) -> User:
        pass

    def delete(self, user_id: uuid) -> User:
        pass

    def find_by_login(self, login):
        for username, password in self.users.items():
            if username == login:
                return User(username, login, password)
        return None
