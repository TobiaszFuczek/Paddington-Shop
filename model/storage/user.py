import uuid
class User:
    def __init__(self, username, password, user_type):
        self.user_id = uuid.uuid4()
        self.username = username
        self.password = password
        self.user_type = user_type