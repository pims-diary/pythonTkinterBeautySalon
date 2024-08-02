from Data.Models.Offering import Offering


class Cart:
    def __init__(self):
        self.items: list[CartItem] = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value


class CartItem:
    def __init__(self):
        self.offering = Offering()
        self.no_of_items = 0

    @property
    def offering(self):
        return self._offering

    @offering.setter
    def offering(self, value):
        self._offering = value

    @property
    def no_of_items(self):
        return self._no_of_items

    @no_of_items.setter
    def no_of_items(self, value):
        self._no_of_items = value

    @property
    def total_price(self):
        return float(self._offering.price) * self._no_of_items
