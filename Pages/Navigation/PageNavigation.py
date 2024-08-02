from enum import Enum, auto


class Feature(Enum):
    HOME = auto()
    ADD_CUSTOMER = auto()
    SEARCH_CUSTOMER = auto()
    CHECKOUT = auto()


def navigate_to(feature_name: Feature, root):
    if feature_name == Feature.HOME:
        from Pages.Home.Home import Home
        home = Home(root)
        home.render_home_page()
    elif feature_name == Feature.ADD_CUSTOMER:
        from Pages.ManageCustomers.AddNewCustomer import AddNewCustomer
        customer = AddNewCustomer(root)
        customer.render_add_new_customer_form()
    elif feature_name == Feature.SEARCH_CUSTOMER:
        from Pages.ManageCustomers.SearchCustomer import SearchCustomer
        search = SearchCustomer(root)
        search.render_search_customer_form()
    elif feature_name == Feature.CHECKOUT:
        from Pages.Checkout.Checkout import Checkout
        checkout = Checkout(root)
        checkout.start_checkout_flow()
