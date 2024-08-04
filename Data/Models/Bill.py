from Data.Models.Cart import Cart


class Bill:
    def __init__(self):
        self.bill_id = 0
        self.customer_id = 0
        self.customer_email = ""
        self.payment_details = ""
        self.cart = Cart()

    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def customer_email(self):
        return self._customer_email

    @customer_email.setter
    def customer_email(self, value):
        self._customer_email = value

    @property
    def payment_details(self):
        return self._payment_details

    @payment_details.setter
    def payment_details(self, value):
        self._payment_details = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
