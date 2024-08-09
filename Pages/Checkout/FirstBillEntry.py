from Data.DataLink.SqlDatabaseToData import create_bill
from Pages.ParentPages.MainMenu import MainMenu
from Pages.ParentPages.PopUpForm import PopUpForm
from Data.Models.Cart import Cart, CartItem
from Data.Models.Bill import Bill


class FirstBillEntry(PopUpForm, MainMenu):
    def __init__(self, root, cart=Cart(), bill=Bill()):
        super().__init__(root)
        self.cart = cart
        self.bill = bill

    def first_bill_entry(self):
        bill_id = 7001
        self.bill.bill_id = bill_id
        self.bill.customer_id = "1005"
        self.cart.customer.id = "1005"
        self.bill.customer_email = "joe@gmail.com"
        self.cart.customer.email = "joe@gmail.com"
        self.bill.payment_details = "Cash"
        self.cart.gift = 20.00
        self.cart.total_amount = 80.00
        cart_item = CartItem()
        cart_item.offering.id = 5001
        cart_item.offering.name = "Haircut for Women with Long Hair"
        cart_item.offering.price = "100.00"
        cart_item.no_of_items = 1
        cart_item.discount = 0.0
        self.cart.items.append(cart_item)
        self.bill.cart = self.cart
        create_bill(self.bill)
