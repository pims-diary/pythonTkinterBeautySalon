class User:
    def __init__(self):
        self.username = ""
        self.password = ""

    @property  # this is also automatically the getter
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property  # this is also automatically the getter
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
