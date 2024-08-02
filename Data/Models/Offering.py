class Offering:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.type = ""
        self.description = ""
        self.price = ""

    @property  # this is also automatically the getter
    def id(self):
        return self._name

    @id.setter
    def id(self, value):
        self._name = value

    @property  # this is also automatically the getter
    def name(self):
        return self._email

    @name.setter
    def name(self, value):
        self._email = value

    @property  # this is also automatically the getter
    def type(self):
        return self._phone

    @type.setter
    def type(self, value):
        self._phone = value

    @property  # this is also automatically the getter
    def description(self):
        return self._type

    @description.setter
    def description(self, value):
        self._type = value

    @property  # this is also automatically the getter
    def price(self):
        return self._is_new

    @price.setter
    def price(self, value):
        self._is_new = value
