from Pages.ParentPages.MainMenu import MainMenu
from Resources.Common.Rules import Discounts
from Resources.Common.Reuse import (validate_fields,
                                    custom_messagebox,
                                    destroy_child_view,
                                    exit_screen,
                                    single_row_table,
                                    single_column_table)
from Data.DataLink.SqlDatabaseToData import search_offering, search_customer
from Data.Models.Offering import Offering
from Data.Models.Cart import Cart
from Data.Models.Customer import Customer
from Controller.Checkout.CheckoutController import (store_offering,
                                                    store_customer,
                                                    sort_cart,
                                                    add_discounts_in_cart,
                                                    calculate_total_amount)
from Pages.ManageCustomers.AddCustomerInCheckout import AddCustomerInCheckout
from Pages.Checkout.PaymentMethod import PaymentMethod
from Pages.Checkout.FirstBillEntry import FirstBillEntry
import tkinter as tk


class Checkout(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Checkout")
        self.root.geometry("1100x600")

        # Frames / sections within Checkout page
        self.item_display_frame = None
        self.customer_display_frame = None
        self.cart_frame = None
        self.proceed_frame = None

        # Windows / Screens outside Checkout page
        self.add_item_screen = None
        self.link_customer_screen = None
        self.add_customer_screen = None

        # Reusable entry field
        self.id_entry = None

        # Data Models
        self.offering = Offering()
        self.cart = Cart()

        # class variables
        self.gift = 0.0
        self.cart_height = 0

    def start_checkout_flow(self):
        # Title label
        title_label = tk.Label(self.root, text="CHECKOUT", font=("Times", 20, "bold"), bg="white", fg="#333333")
        title_label.pack()

        # Cart items frame
        self.cart_frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.cart_frame.pack()

        # Add button
        add_button = tk.Button(self.root, text="ADD ITEM", command=self.add_item,
                               font=("Times", 10, "bold"), bg="#4caf50", fg="#ffffff")
        add_button.pack()

        # Link a Customer button
        add_button = tk.Button(self.root, text="LINK A CUSTOMER", command=self.link_customer,
                               font=("Times", 10, "bold"), bg="#4caf50", fg="#ffffff")
        add_button.pack()

        # Proceed to payment section
        self.proceed_frame = tk.Frame(self.root)
        self.proceed_frame.pack()

    def add_item(self):
        """
        Add an item to the cart.
        User is navigated away to Search an item to add.
        After search completion, User is returned back
        to the Checkout page and the added cart item is
        displayed.
        """
        self.add_item_screen = tk.Toplevel(self.root)
        self.add_item_screen.title("Search item")
        self.add_item_screen.geometry("600x600")
        self.add_item_screen.configure(bg="white")

        title_label = tk.Label(self.add_item_screen, text="Search item", font=("Helvetica", 18, "bold"), bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        # Customer name label and entry
        name_label = tk.Label(self.add_item_screen, text="Item ID",
                              font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        name_label.pack(pady=10)
        self.id_entry = tk.Entry(self.add_item_screen, font=("Helvetica", 10))
        self.id_entry.pack(pady=7)

        # Search button
        search_button = tk.Button(self.add_item_screen, text="Search",
                                  font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                  command=self.search_offering)
        search_button.pack(pady=50)

        self.item_display_frame = tk.Frame(self.add_item_screen)
        self.item_display_frame.pack()

    def search_offering(self):
        """
        User is navigated away to Search an item to add to cart.
        The function caters to a successful search and multiple
        possible error scenarios for searching an offering.
        """
        destroy_child_view(self.item_display_frame)

        if not validate_fields((self.id_entry,)):
            custom_messagebox("Blank Field Error", "Cannot leave Item ID field blank", "error")
            return

        try:
            offering_id = int(self.id_entry.get())
        except TypeError:
            custom_messagebox("Format Error", "Item ID field must be a whole number", "error")
            return

        offering_info = search_offering(offering_id)

        if len(offering_info) == 0:
            custom_messagebox("No results", "An Item with this Item ID was not found", "error")
            return
        else:
            item = offering_info[0]
            column_names = ["Id", "Name", "Type", "Description", "Price"]
            table_frame = tk.Frame(self.item_display_frame)
            table_frame.pack()
            single_column_table(table_frame, item, column_names)

            add_to_cart_button = tk.Button(self.item_display_frame, text="ADD TO CART", command=self.add_to_cart,
                                           font=("Times", 10, "bold"), bg="#4caf50", fg="#ffffff")
            add_to_cart_button.pack()

            self.offering = store_offering(item)

    def add_to_cart(self):
        """
        Adding of item to cart is performed.
        The new window to search is destroyed on task completion.
        """
        self.cart.items = sort_cart(self.offering, self.cart.items, 1)
        exit_screen(self.add_item_screen)

        self.render_cart_items()

    def link_customer(self):
        if len(self.cart.items) == 0:
            custom_messagebox("Empty Cart", "You must add atleast one item to cart before linking a customer", "error")
            return

        self.link_customer_screen = tk.Toplevel(self.root)
        self.link_customer_screen.title("Link a customer")
        self.link_customer_screen.geometry("600x600")
        self.link_customer_screen.configure(bg="white")

        title_label = tk.Label(self.link_customer_screen, text="Link a Customer", font=("Helvetica", 18, "bold"),
                               bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        # Customer name label and entry
        id_label = tk.Label(self.link_customer_screen, text="Customer ID",
                            font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        id_label.pack(pady=10)
        self.id_entry = tk.Entry(self.link_customer_screen, font=("Helvetica", 10))
        self.id_entry.pack(pady=7)

        # Search button
        search_button = tk.Button(self.link_customer_screen, text="Search",
                                  font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                  command=self.search_customer)
        search_button.pack(pady=50)

        self.customer_display_frame = tk.Frame(self.link_customer_screen)
        self.customer_display_frame.pack()

    def search_customer(self):
        destroy_child_view(self.customer_display_frame)

        if not validate_fields((self.id_entry,)):
            custom_messagebox("Blank Field Error", "Cannot leave Customer ID field blank", "error")
            return

        try:
            customer_id = int(self.id_entry.get())
        except TypeError:
            custom_messagebox("Format Error", "Customer ID field must be a whole number", "error")
            return

        customer_info = search_customer(customer_id)

        if len(customer_info) == 0:
            not_found_error = tk.Label(self.customer_display_frame, text="No Customer with this ID was found.")
            not_found_error.pack(pady=7)
            question = tk.Label(self.customer_display_frame, text="Do you want to create a new Customer?")
            question.pack(pady=7)
            tk.Button(self.customer_display_frame, text="CREATE CUSTOMER", command=self.add_customer,
                      font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff").pack()
        else:
            column_names = ["Id", "Name", "Email", "Phone", "Member Type", "Not Ordered Before?"]

            table_frame = tk.Frame(self.customer_display_frame)
            table_frame.pack()
            single_row_table(table_frame, customer_info[0], column_names)

            link_this_customer_button = tk.Button(self.customer_display_frame, text="LINK THIS CUSTOMERS",
                                                  command=lambda: self.add_and_link_customer(self.cart.customer),
                                                  font=("Times", 10, "bold"), bg="#4caf50", fg="#ffffff")
            link_this_customer_button.pack()

            self.cart.customer = store_customer(customer_info[0])

    def add_customer(self):
        self.add_customer_screen = tk.Toplevel(self.root)
        self.add_customer_screen.title = "Add new Customer"
        self.add_customer_screen.geometry("600x600")
        self.add_customer_screen.configure(bg="white")

        screen = AddCustomerInCheckout(self.root)
        screen.render_add_customer_pop_up(self.add_customer_screen, self)

    def add_and_link_customer(self, customer: Customer):
        exit_screen(self.add_customer_screen)
        exit_screen(self.link_customer_screen)

        self.cart.customer = customer
        table_frame = tk.Frame(self.proceed_frame)
        table_frame.pack()

        tk.Label(table_frame, text="Id", font='Helvetica 10 bold').grid(row=0, column=0)
        tk.Label(table_frame, text=self.cart.customer.id).grid(row=1, column=0)
        tk.Label(table_frame, text="Name", font='Helvetica 10 bold').grid(row=0, column=1)
        tk.Label(table_frame, text=self.cart.customer.name).grid(row=1, column=1)
        tk.Label(table_frame, text="Email", font='Helvetica 10 bold').grid(row=0, column=2)
        tk.Label(table_frame, text=self.cart.customer.email).grid(row=1, column=2)
        tk.Label(table_frame, text="Phone", font='Helvetica 10 bold').grid(row=0, column=3)
        tk.Label(table_frame, text=self.cart.customer.phone).grid(row=1, column=3)
        tk.Label(table_frame, text="Type", font='Helvetica 10 bold').grid(row=0, column=4)
        tk.Label(table_frame, text=self.cart.customer.type).grid(row=1, column=4)

        tk.Button(self.proceed_frame, text="PROCEED TO PAY",
                  command=self.proceed_to_pay, pady=10,
                  font=("Times", 10, "bold"), bg="#4caf50", fg="#ffffff").pack()

        cart_changes = add_discounts_in_cart(self.cart.items, self.cart.customer)

        if cart_changes is None:
            custom_messagebox("Server Error",
                              "Oops, there is something wrong with the data. Please contact the app admin",
                              "error")
        else:
            self.cart.items = cart_changes

        self.render_cart_items()

    def render_cart_items(self):
        destroy_child_view(self.cart_frame)

        height = len(self.cart.items)
        for i in range(height):
            tk.Label(self.cart_frame, text=self.cart.items[i].offering.name).grid(row=i, column=0)
            tk.Label(self.cart_frame, text="$" + str(self.cart.items[i].offering.price)).grid(row=i, column=1)
            tk.Label(self.cart_frame, text=self.cart.items[i].no_of_items).grid(row=i, column=3)
            if self.cart.items[i].discount == 0.0:
                discount = 'N/A'
                comments = ""
            else:
                discount = str(self.cart.items[i].discount) + "%"
                offering_type = self.cart.items[i].offering.type + "s"
                customer_type = self.cart.customer.type + " members"
                comments = discount + " discount for " + customer_type + " on " + offering_type
            tk.Label(self.cart_frame, text=discount).grid(row=i, column=4)
            tk.Label(self.cart_frame, text="$" + str(self.cart.items[i].total_price)).grid(row=i, column=5)
            tk.Label(self.cart_frame, text=comments).grid(row=i, column=6)

        tk.Label(self.cart_frame, text="Gift: ").grid(row=height + 1, column=0)
        if self.cart.customer.is_new:
            gift = "20.00"
            self.cart.gift = Discounts.NEW_CUSTOMER_GIFT_AMOUNT
        else:
            gift = "0.00"
            self.cart.gift = Discounts.OLD_CUSTOMER_GIFT_AMOUNT

        tk.Label(self.cart_frame, text="$" + str(gift)).grid(row=height + 1, column=2)

        tk.Label(self.cart_frame, text="Total Amount: ").grid(row=height + 2, column=0)
        self.cart.total_amount = calculate_total_amount(self.cart.items, self.cart.customer)
        tk.Label(self.cart_frame, text="$" + str(self.cart.total_amount)).grid(row=height + 2, column=2)

    def proceed_to_pay(self):
        PaymentMethod(self.root, self.cart)

    def create_first_entry(self):
        entry = FirstBillEntry(self.root)
        entry.first_bill_entry()
