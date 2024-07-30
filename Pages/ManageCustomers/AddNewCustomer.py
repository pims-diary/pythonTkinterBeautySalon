from tkinter import *
from tkinter import ttk
import tkinter as tk
from Pages.MainMenu.MainMenu import MainMenu
from Controller.ManageCustomers.CustomersController import validate_fields, perform_add_customer
from Resources.Common.Reuse import custom_messagebox, combo_selection
from Data.Models.Customer import Customer

customer_type = ["Guest", "Silver", "Gold", "Platinum"]


class AddNewCustomer(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Add New Customer")
        self.name_entry = None
        self.email_entry = None
        self.phone_entry = None
        self.type_entry = None

    def render_add_new_customer_form(self):
        title_label = tk.Label(self.root, text="ADD NEW CUSTOMER", font=("Times", 20, "bold"), bg="#add8e6", fg="#333333")
        title_label.pack(pady=15)

        # Customer name label and entry
        name_label = tk.Label(self.root, text="Customer Name", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        name_label.pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.name_entry.pack(pady=7)

        # Customer Email label and entry
        email_label = tk.Label(self.root, text="Email", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        email_label.pack(pady=10)
        self.email_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.email_entry.pack(pady=7)

        # Customer Phone label and entry
        phone_label = tk.Label(self.root, text="Phone number", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        phone_label.pack(pady=10)
        self.phone_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.phone_entry.pack(pady=7)

        # Customer Type label and entry
        type_label = tk.Label(self.root, text="Customer Type", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        type_label.pack(pady=10)
        self.type_entry = ttk.Combobox(self.root, values=customer_type)
        self.type_entry.current(1)
        self.type_entry.bind("<<ComboboxSelected>>")
        self.type_entry.pack()

        # Add button
        add_button = tk.Button(self.root, text="Add", font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                               command=self.add_new)
        add_button.pack(pady=50)

    def add_new(self):
        if not validate_fields(self.name_entry, self.email_entry, self.phone_entry):
            custom_messagebox("Blank Field Error", "Cannot leave username or password field blank", "error")
            return

        customer = Customer()
        customer.name = self.name_entry.get()
        customer.email = self.email_entry.get()
        customer.phone = self.phone_entry.get()
        customer.type = self.type_entry.get()

        perform_add_customer(customer)
