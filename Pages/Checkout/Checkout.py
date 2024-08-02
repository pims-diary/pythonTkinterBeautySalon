from Pages.MainMenu.MainMenu import MainMenu
from Resources.Common.Reuse import validate_fields, custom_messagebox, destroy_child_view, exit_screen, make_table
from Data.DataLink.SqlDatabaseToData import search_offering, search_customer
from Data.Models.Offering import Offering
from Data.Models.Cart import Cart, CartItem
from Controller.Checkout.CheckoutController import store_offering, sort_cart
import tkinter as tk
import tksheet


class Checkout(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.sheet = tksheet.Sheet(self.root)
        self.search_entry = None
        self.id_entry = None
        self.item_display_frame = None
        self.customer_display_frame = None
        self.add_item_screen = None
        self.offering = Offering()
        self.cart_item = CartItem()
        self.cart = Cart()
        self.cart_height = 0
        self.cart_frame = None
        self.link_customer_screen = None

    def start_checkout_flow(self):
        # Title label
        title_label = tk.Label(self.root, text="CHECKOUT", font=("Times", 20, "bold"), bg="white", fg="#333333")
        title_label.pack()

        # Cart items frame
        self.cart_frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=1)
        self.cart_frame.pack()

        # Datatable to display Added offerings

        # Add button
        add_button = tk.Button(self.root, text="ADD ITEM", command=self.add_item)
        add_button.pack()

        # Remove button
        remove_button = tk.Button(self.root, text="REMOVE")
        remove_button.pack()

        # Link a Customer button
        add_button = tk.Button(self.root, text="LINK A CUSTOMER", command=self.link_customer)
        add_button.pack()

    def add_item(self):
        self.add_item_screen = tk.Toplevel(self.root)
        self.add_item_screen.title("Search item")
        self.add_item_screen.geometry("600x400")
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
            height = 1
            width = 5
            item = offering_info[0]
            make_table(height, width, self.item_display_frame, item)

            add_to_cart_button = tk.Button(self.item_display_frame, text="ADD TO CART", command=self.add_to_cart)
            add_to_cart_button.grid(row=2)

            self.offering = store_offering(item)

    def add_to_cart(self):
        self.cart.items = sort_cart(self.offering, self.cart.items, 1)
        exit_screen(self.add_item_screen)

        destroy_child_view(self.cart_frame)

        height = len(self.cart.items)
        for i in range(height):
            tk.Label(self.cart_frame, text=self.cart.items[i].offering.name).grid(row=i, column=0)
            tk.Label(self.cart_frame, text=self.cart.items[i].offering.price).grid(row=i, column=1)
            tk.Label(self.cart_frame, text=self.cart.items[i].no_of_items).grid(row=i, column=3)
            tk.Label(self.cart_frame, text=self.cart.items[i].total_price).grid(row=i, column=4)

    def link_customer(self):
        self.add_item_screen = tk.Toplevel(self.root)
        self.add_item_screen.title("Link a customer")
        self.add_item_screen.geometry("600x400")
        self.add_item_screen.configure(bg="white")

        title_label = tk.Label(self.add_item_screen, text="Link a Customer", font=("Helvetica", 18, "bold"),
                               bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        # Customer name label and entry
        id_label = tk.Label(self.add_item_screen, text="Customer ID",
                            font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        id_label.pack(pady=10)
        self.id_entry = tk.Entry(self.add_item_screen, font=("Helvetica", 10))
        self.id_entry.pack(pady=7)

        # Search button
        search_button = tk.Button(self.add_item_screen, text="Search",
                                  font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                  command=self.search_customer)
        search_button.pack(pady=50)

        self.customer_display_frame = tk.Frame(self.add_item_screen)
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
            tk.Button(self.customer_display_frame, text="CREATE CUSTOMER", command=self.add_customer)
        else:
            height = 1
            width = 5
            item = customer_info[0]
            make_table(height, width, self.item_display_frame, item)

            add_to_cart_button = tk.Button(self.item_display_frame, text="LINK THIS CUSTOMERS",
                                           command=self.execute_customer_link)
            add_to_cart_button.grid(row=2)

            self.offering = store_offering(item)

    def execute_customer_link(self):
        pass

    def add_customer(self):
        pass

        # self.sheet.grid()
        # self.sheet.set_sheet_data([[f"{ri + cj}" for cj in range(4)] for ri in range(1)])
        # table enable choices listed below:
        # self.sheet.enable_bindings(("single_select",
        #                        "row_select",
        #                        "column_width_resize",
        #                        "arrowkeys",
        #                        "right_click_popup_menu",
        #                        "rc_select",
        #                        "rc_insert_row",
        #                        "rc_delete_row",
        #                        "copy",
        #                        "cut",
        #                        "paste",
        #                        "delete",
        #                        "undo",
        #                        "edit_cell"))
