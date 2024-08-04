from enum import Enum, auto


class Feature(Enum):
    HOME = auto()
    ADD_CUSTOMER = auto()
    SEARCH_CUSTOMER = auto()
    CHECKOUT = auto()
    SEARCH_BILL = auto()


def navigate_to(feature_name: Feature, root):
    if feature_name == Feature.HOME:
        from Pages.Home.Home import Home
        Home(root)
    elif feature_name == Feature.ADD_CUSTOMER:
        from Pages.ManageCustomers.AddCustomer import AddCustomer
        customer = AddCustomer(root)
        customer.render_add_new_customer_form()
    elif feature_name == Feature.SEARCH_CUSTOMER:
        from Pages.ManageCustomers.SearchCustomer import SearchCustomer
        search = SearchCustomer(root)
        search.render_search_customer_form()
    elif feature_name == Feature.CHECKOUT:
        from Pages.Checkout.Checkout import Checkout
        checkout = Checkout(root)
        checkout.start_checkout_flow()
    elif feature_name == Feature.SEARCH_BILL:
        from Pages.ManageBill.SearchBill import SearchBill
        SearchBill(root)
