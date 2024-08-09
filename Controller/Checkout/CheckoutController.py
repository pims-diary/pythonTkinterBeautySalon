from Data.Models.Offering import Offering
from Data.Models.Customer import Customer
from Data.Models.Cart import CartItem
from Data.Models.Cart import Cart
from Data.Models.Bill import Bill
from Resources.Common.Rules import Discounts
from Data.DataLink.SqlDatabaseToData import create_bill, get_last_bill_id


def store_offering(item):
    offering = Offering()

    offering.id = item[0]
    offering.name = item[1]
    offering.type = item[2]
    offering.description = item[3]
    offering.price = item[4]

    return offering


def store_customer(data):
    customer = Customer()

    customer.id = data[0]
    customer.name = data[1]
    customer.email = data[2]
    customer.phone = data[3]
    customer.type = data[4]
    customer.is_new = data[5]

    return customer


def sort_cart(offering: Offering, items: list[CartItem], added_quantity: int):
    """Sort items to cart
                If the offering to be added already exists,
                then increase the number of items for the offering,
                else add the offering as a new cart item"""
    for item in items:
        if item.offering.id == offering.id:
            item.no_of_items = item.no_of_items + added_quantity
            return items
    cart_item = CartItem()
    cart_item.offering = offering
    cart_item.no_of_items = added_quantity
    items.append(cart_item)
    return items


def add_discounts_in_cart(items: list[CartItem], customer: Customer):
    """
    Add discounts to each item based on
    - the customer type,
    - the item type,
    """
    # Control structure: Conditional implementation
    # Check if Member
    if not customer.type == "Guest":
        # if Member, check Product / Service
        for item in items:
            if item.offering.type == "Product":
                # Flat 10% (customisable) discount on products for all members
                item.discount = Discounts.PRODUCT_DISCOUNT_PERCENT
            elif item.offering.type == "Service":
                if customer.type == "Premium":
                    # 20% discount on services for Premium customers
                    item.discount = Discounts.SERVICE_DISCOUNT_FOR_PREMIUM_PERCENT
                elif customer.type == "Gold":
                    # 15% discount on services for Gold customers
                    item.discount = Discounts.SERVICE_DISCOUNT_FOR_GOLD_PERCENT
                elif customer.type == "Silver":
                    # 10% discount on services for Silver customers
                    item.discount = Discounts.SERVICE_DISCOUNT_FOR_SILVER_PERCENT
                else:
                    # Database error in Customer type
                    return None
            else:
                # Database error in Item type
                return None

    return items


def calculate_total_amount(items: list[CartItem], customer: Customer):
    """
    Calculate the total amount the customer has to pay
    """
    total_amount = 0.0

    # Calculate the sum of the total price for each offering
    # with multiple items possible in each of them
    for item in items:
        total_amount = total_amount + item.total_price

    # Deduct gift amount from total amount, if applicable
    if customer.is_new:
        total_amount = total_amount - Discounts.NEW_CUSTOMER_GIFT_AMOUNT

    return total_amount


def insert_new_bill(payment_details: str, cart: Cart):
    bill_id = generate_bill_id()
    bill = Bill()
    bill.bill_id = bill_id
    bill.customer_id = cart.customer.id
    bill.customer_email = cart.customer.email
    bill.payment_details = payment_details
    bill.cart = cart
    is_success = create_bill(bill)
    # Data Structure: Tuple implementation
    return is_success, bill_id


def generate_bill_id():
    bill_id = get_last_bill_id()
    bill_id = bill_id + 1
    return bill_id


def calculate_balance(cash_amount, total_amount):
    return cash_amount - total_amount
