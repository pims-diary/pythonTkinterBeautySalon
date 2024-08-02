from Data.Models.Offering import Offering


class Cart:
    def __init__(self):
        self.items: list[Offering] = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
