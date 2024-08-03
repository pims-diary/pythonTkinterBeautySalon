class Customer:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.email = ""
        self.phone = ""
        self.type = ""
        self.is_new = False

    @property  # this is also automatically the getter
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property  # this is also automatically the getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property  # this is also automatically the getter
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property  # this is also automatically the getter
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property  # this is also automatically the getter
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property  # this is also automatically the getter
    def is_new(self):
        return self._is_new

    @is_new.setter
    def is_new(self, value):
        self._is_new = value
