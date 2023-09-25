import uuid

from model.storage.user import User


class UserStorage:
    def __init__(self):
        self.users = {
            "owner": User("owner", "owner", "owner"),
            "personnel": User("personnel", "personnel", "personnel"),
            "user": User("user", "user", "user"),
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
        for user in self.users.values():
            if user.username == login:
                return user
        return None
