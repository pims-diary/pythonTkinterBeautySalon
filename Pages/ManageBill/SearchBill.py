import tkinter as tk
from Pages.ParentPages.MainMenu import MainMenu
from Data.DataLink.SqlDatabaseToData import fetch_bill
from Resources.Common.Reuse import custom_messagebox, validate_fields, destroy_child_view
from Resources.Common.Rules import Discounts
from Controller.Checkout.CheckoutController import calculate_total_amount


class SearchBill(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Search Bill")
        self.root.geometry("600x550")
        self.bill = None

        # Frames
        self.frame = None
        self.bill_details_frame = None
        self.summary_header_frame = None
        self.order_details_frame = None

        # Entry
        self.id_entry = None

        self.render_search_bill_form()

    def render_search_bill_form(self):
        title_label = tk.Label(self.root,
                               text="SEARCH BILL",
                               font=("Times", 20, "bold"),
                               bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=15)

        # Customer name label and entry
        name_label = tk.Label(self.root, text="Bill ID", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        name_label.pack(pady=10)
        self.id_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.id_entry.pack(pady=7)

        # Search button
        add_button = tk.Button(self.root, text="Search", font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                               command=self.search)
        add_button.pack(pady=50)

        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.bill_details_frame = tk.Frame(self.frame)
        self.bill_details_frame.pack()
        self.summary_header_frame = tk.Frame(self.frame)
        self.summary_header_frame.pack()
        self.order_details_frame = tk.Frame(self.frame)
        self.order_details_frame.pack()

    def search(self):
        if not validate_fields((self.id_entry,)):
            custom_messagebox("Blank Field Error", "Cannot leave Bill ID field blank", "error")
            return

        try:
            customer_id = int(self.id_entry.get())
        except TypeError:
            custom_messagebox("Format Error", "Bill ID field must be a whole number", "error")
            return

        self.bill = fetch_bill(customer_id)

        if self.bill is None:
            custom_messagebox("No results", "A Bill with this Bill ID was not found", "error")
            return
        else:
            self.render_bill_details()
            self.render_order_summary()

    def render_bill_details(self):
        destroy_child_view(self.bill_details_frame)

        tk.Label(self.bill_details_frame, text="Bill Id", font='Helvetica 10 bold').grid(row=0, column=0)
        tk.Label(self.bill_details_frame, text=self.bill.bill_id).grid(row=0, column=1)
        tk.Label(self.bill_details_frame, text="Customer Id", font='Helvetica 10 bold').grid(row=1, column=0)
        tk.Label(self.bill_details_frame, text=self.bill.customer_id).grid(row=1, column=1)
        tk.Label(self.bill_details_frame, text="Email", font='Helvetica 10 bold').grid(row=2, column=0)
        tk.Label(self.bill_details_frame, text=self.bill.customer_email).grid(row=2, column=1)
        tk.Label(self.bill_details_frame, text="Payment Details", font='Helvetica 10 bold').grid(row=3, column=0)
        tk.Label(self.bill_details_frame, text=self.bill.payment_details).grid(row=3, column=1)

    def render_order_summary(self):
        destroy_child_view(self.order_details_frame)

        name_label = tk.Label(self.summary_header_frame, text="Order Summary",
                              font=("Times", 18, "bold"), bg="#add8e6", fg="#333333", width=600)
        name_label.pack(pady=10)

        cart = self.bill.cart
        height = len(cart.items)
        for i in range(height):
            tk.Label(self.order_details_frame, text=cart.items[i].offering.name).grid(row=i, column=0)
            tk.Label(self.order_details_frame, text="$" + str(cart.items[i].offering.price)).grid(row=i, column=1)
            tk.Label(self.order_details_frame, text=cart.items[i].no_of_items).grid(row=i, column=3)
            if cart.items[i].discount == 0.0:
                discount = 'N/A'
                comments = ""
            else:
                discount = str(cart.items[i].discount) + "%"
                offering_type = cart.items[i].offering.type + "s"
                customer_type = cart.customer.type + " members"
                comments = discount + " discount for " + customer_type + " on " + offering_type
            tk.Label(self.order_details_frame, text=discount).grid(row=i, column=4)
            tk.Label(self.order_details_frame, text="$" + str(cart.items[i].total_price)).grid(row=i, column=5)
            tk.Label(self.order_details_frame, text=comments).grid(row=i, column=6)

        tk.Label(self.order_details_frame, text="Gift: ").grid(row=height + 1, column=0)
        if cart.customer.is_new:
            gift = "20.00"
            cart.gift = Discounts.NEW_CUSTOMER_GIFT_AMOUNT
        else:
            gift = "0.00"
            cart.gift = Discounts.OLD_CUSTOMER_GIFT_AMOUNT

        tk.Label(self.order_details_frame, text="$" + str(gift)).grid(row=height + 1, column=2)

        tk.Label(self.order_details_frame, text="Total Amount: ").grid(row=height + 2, column=0)
        cart.total_amount = calculate_total_amount(cart.items, cart.customer)
        tk.Label(self.order_details_frame, text="$" + str(cart.total_amount)).grid(row=height + 2, column=2)
