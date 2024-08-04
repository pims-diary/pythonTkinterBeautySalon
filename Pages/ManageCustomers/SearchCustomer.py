import tkinter as tk
from Pages.ParentPages.MainMenu import MainMenu
from Data.DataLink.SqlDatabaseToData import search_customer
from Resources.Common.Reuse import custom_messagebox, validate_fields, destroy_child_view, single_row_table


class SearchCustomer(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Search Customer")
        self.id_entry = None
        self.frame = None

    def render_search_customer_form(self):
        title_label = tk.Label(self.root,
                               text="SEARCH CUSTOMER",
                               font=("Times", 20, "bold"),
                               bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=15)

        # Customer name label and entry
        name_label = tk.Label(self.root, text="Customer ID", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        name_label.pack(pady=10)
        self.id_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.id_entry.pack(pady=7)

        # Search button
        add_button = tk.Button(self.root, text="Search", font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                               command=self.search)
        add_button.pack(pady=50)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

    def search(self):
        destroy_child_view(self.frame)

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
            custom_messagebox("No results", "A Customer with this Customer ID was not found", "error")
            return
        else:
            column_names = ["Id", "Name", "Email", "Phone", "Member Type", "Not Ordered Before?"]
            single_row_table(self.frame, customer_info[0], column_names)
