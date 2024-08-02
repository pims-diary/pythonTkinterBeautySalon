import tkinter as tk
from Pages.Navigation.PageNavigation import navigate_to, Feature
from Pages.Common.Form import Form


class Toolbar:
    def __init__(self, root):
        self.root = root
        self.menu_bar = None
        self.toolbar_menu = None
        self.toolbar_customers = None
        self.toolbar_offerings = None

    def render_toolbar(self):
        """Display the main menu / dashboard after successful login"""

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.toolbar_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu", menu=self.toolbar_menu)

        self.toolbar_menu.add_command(label="Home", command=self.home)
        self.toolbar_menu.add_command(label="Checkout", command=self.checkout)
        self.toolbar_menu.add_command(label="Billing", command=self.billing)
        self.toolbar_menu.add_separator()
        self.toolbar_menu.add_command(label="Exit", command=self.root.quit)

        self.toolbar_customers = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Customers", menu=self.toolbar_customers)

        self.toolbar_customers.add_command(label="Add Customer", command=self.add_customer)
        self.toolbar_customers.add_command(label="Search Customer", command=self.search_customer)
        self.toolbar_customers.add_command(label="Members", command=self.members)

        self.toolbar_offerings = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Offerings", menu=self.toolbar_offerings)

        self.toolbar_offerings.add_command(label="Services", command=self.services)
        self.toolbar_offerings.add_command(label="Products", command=self.products)

    def home(self):
        navigate_to(Feature.HOME, self.root)

    def checkout(self):
        navigate_to(Feature.CHECKOUT, self.root)

    def add_customer(self):
        navigate_to(Feature.ADD_CUSTOMER, self.root)

    def search_customer(self):
        navigate_to(Feature.SEARCH_CUSTOMER, self.root)

    def services(self):
        """Open Services form"""
        Form(self.root, "Services")

    def products(self):
        """Open Products form"""
        Form(self.root, "Products")

    def members(self):
        """Open Members form"""
        Form(self.root, "Members")

    def billing(self):
        """Open Billing form"""
        Form(self.root, "Billing")
