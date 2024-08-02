from Data.Models.Offering import Offering
from Data.Models.Cart import CartItem


def store_offering(item):
    offering = Offering()

    offering.id = item[0]
    offering.name = item[1]
    offering.type = item[2]
    offering.description = item[3]
    offering.price = item[4]

    return offering


def sort_cart(offering: Offering, items: list[CartItem], added_quantity: int):
    for item in items:
        if item.offering.id == offering.id:
            item.no_of_items = item.no_of_items + added_quantity
            return items
    cart_item = CartItem()
    cart_item.offering = offering
    cart_item.no_of_items = added_quantity
    items.append(cart_item)
    return items
