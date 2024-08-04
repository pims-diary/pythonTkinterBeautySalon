from Data.Models.Offering import Offering
from Data.Models.Customer import Customer


class Cart:
    def __init__(self):
        self.items: list[CartItem] = []
        self.gift = 0.0
        self.total_amount = 0.0
        self.customer = Customer()

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def gift(self):
        return self._gift

    @gift.setter
    def gift(self, value):
        self._gift = value

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value


class CartItem:
    def __init__(self):
        self.offering = Offering()
        self.no_of_items = 0
        self.discount = 0.0

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
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = float(value)

    @property
    def total_price(self):
        return (float(self._offering.price) * self._no_of_items) * (100.0 - float(self._discount)) / 100.0
