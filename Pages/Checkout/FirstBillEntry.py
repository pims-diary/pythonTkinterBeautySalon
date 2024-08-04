from Data.DataLink.SqlDatabaseToData import create_bill
from Data.Models.Bill import Bill
from Data.Models.Cart import Cart, CartItem


def first_bill_entry():
    bill_id = 7001
    bill = Bill()
    cart = Cart()
    bill.bill_id = bill_id
    bill.customer_id = "1005"
    cart.customer.id = "1005"
    bill.customer_email = "joe@gmail.com"
    cart.customer.email = "joe@gmail.com"
    bill.payment_details = "Cash"
    cart.gift = 20.00
    cart.total_amount = 80.00
    cart_item = CartItem()
    cart_item.offering.id = 5001
    cart_item.offering.name = "Haircut for Women with Long Hair"
    cart_item.offering.price = "100.00"
    cart_item.no_of_items = 1
    cart_item.discount = 0.0
    cart.items.append(cart_item)
    bill.cart = cart
    is_success = create_bill(bill)
    print(is_success)
