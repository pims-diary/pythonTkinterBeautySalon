import tkinter as tk
from tkinter import ttk
from Resources.Common.Reuse import validate_fields, custom_messagebox
from Data.Models.Customer import Customer
from Data.DataLink.SqlDatabaseToData import get_last_customer
from Controller.ManageCustomers.CustomersController import perform_add_customer


customer_type = ["Guest", "Silver", "Gold", "Premium"]


class AddCustomerInCheckout:
    def __init__(self, root):
        self.root = root
        self.pop_up_screen = None
        self.name_entry = None
        self.email_entry = None
        self.phone_entry = None
        self.type_entry = None
        self.customer = Customer()

    def render_add_customer_pop_up(self, add_customer_screen, checkout_obj):
        self.pop_up_screen = add_customer_screen
        title_label = tk.Label(self.pop_up_screen,
                               text="ADD NEW CUSTOMER",
                               font=("Times", 20, "bold"),
                               bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=15)

        # Customer name label and entry
        name_label = tk.Label(self.pop_up_screen, text="Customer Name", font=("Times", 18, "bold"), bg="#add8e6",
                              fg="#333333")
        name_label.pack(pady=10)
        self.name_entry = tk.Entry(self.pop_up_screen, font=("Helvetica", 10))
        self.name_entry.pack(pady=7)

        # Customer Email label and entry
        email_label = tk.Label(self.pop_up_screen, text="Email", font=("Times", 18, "bold"), bg="#add8e6",
                               fg="#333333")
        email_label.pack(pady=10)
        self.email_entry = tk.Entry(self.pop_up_screen, font=("Helvetica", 10))
        self.email_entry.pack(pady=7)

        # Customer Phone label and entry
        phone_label = tk.Label(self.pop_up_screen, text="Phone number", font=("Times", 18, "bold"), bg="#add8e6",
                               fg="#333333")
        phone_label.pack(pady=10)
        self.phone_entry = tk.Entry(self.pop_up_screen, font=("Helvetica", 10))
        self.phone_entry.pack(pady=7)

        # Customer Type label and entry
        type_label = tk.Label(self.pop_up_screen, text="Customer Type", font=("Times", 18, "bold"), bg="#add8e6",
                              fg="#333333")
        type_label.pack(pady=10)
        self.type_entry = ttk.Combobox(self.pop_up_screen, values=customer_type)
        self.type_entry.current(1)
        self.type_entry.bind("<<ComboboxSelected>>")
        self.type_entry.pack()

        # Add button
        add_button = tk.Button(self.pop_up_screen, text="Add", font=("Times", 16, "bold"), bg="#4caf50",
                               fg="#ffffff", command=lambda: self.add_and_link(checkout_obj))
        add_button.pack(pady=50)

    def add_and_link(self, checkout_screen):
        if not validate_fields((self.name_entry, self.email_entry, self.phone_entry)):
            custom_messagebox("Blank Field Error", "Cannot leave username or password field blank", "error")
            return

        customer = Customer()
        customer.name = self.name_entry.get()
        customer.email = self.email_entry.get()
        customer.phone = self.phone_entry.get()
        customer.type = self.type_entry.get()
        customer.is_new = True

        is_success = perform_add_customer(customer)

        if not is_success:
            custom_messagebox("Server Error", "Oops, something went wrong. Please try again.", "error")
        else:
            self.customer = get_last_customer()
            checkout_screen.add_and_link_customer(self.customer)
            custom_messagebox("Success", "The Customer was successfully added!", "info")
