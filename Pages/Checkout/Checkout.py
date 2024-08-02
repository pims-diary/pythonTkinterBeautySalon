from Pages.MainMenu.MainMenu import MainMenu
from Resources.Common.Reuse import validate_fields, custom_messagebox, destroy_child_view, exit_screen, make_table
from Data.DataLink.SqlDatabaseToData import search_offering
from Data.Models.Offering import Offering
from Data.Models.Cart import Cart
import tkinter as tk
import tksheet


class Checkout(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.sheet = tksheet.Sheet(self.root)
        self.search_entry = None
        self.id_entry = None
        self.item_id_entry = None
        self.frame = None
        self.add_item_screen = None
        self.offering = Offering()
        self.cart = Cart()

    def start_checkout_flow(self):
        # Title label
        title_label = tk.Label(self.root, text="CHECKOUT", font=("Times", 20, "bold"), bg="white", fg="#333333")
        title_label.pack()

        # Cart items frame
        cart_frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=1)
        cart_frame.pack()

        # Datatable to display Added offerings

        # Add button
        add_button = tk.Button(self.root, text="ADD ITEM", command=self.add_item)
        add_button.pack()

        # Remove button
        remove_button = tk.Button(self.root, text="REMOVE")
        remove_button.pack()

    def add_item(self):
        self.add_item_screen = tk.Toplevel(self.root)
        self.add_item_screen.title("Search item")
        self.add_item_screen.geometry("600x400")
        self.add_item_screen.configure(bg="white")

        title_label = tk.Label(self.add_item_screen, text="Search item", font=("Helvetica", 18, "bold"), bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        # Customer name label and entry
        name_label = tk.Label(self.add_item_screen, text="Item ID", font=("Times", 18, "bold"), bg="#add8e6", fg="#333333")
        name_label.pack(pady=10)
        self.item_id_entry = tk.Entry(self.add_item_screen, font=("Helvetica", 10))
        self.item_id_entry.pack(pady=7)

        # Search button
        search_button = tk.Button(self.add_item_screen, text="Search", font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                  command=self.search)
        search_button.pack(pady=50)

        self.frame = tk.Frame(self.add_item_screen)
        self.frame.pack()

    def search(self):
        destroy_child_view(self.frame)

        if not validate_fields((self.item_id_entry,)):
            custom_messagebox("Blank Field Error", "Cannot leave Item ID field blank", "error")
            return

        try:
            offering_id = int(self.item_id_entry.get())
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
            make_table(height, width, self.frame, item)

            add_to_cart_button = tk.Button(self.frame, text="ADD TO CART")
            add_to_cart_button.grid(row=2)

            self.offering.id = item[0]
            self.offering.name = item[1]
            self.offering.type = item[2]
            self.offering.description = item[3]
            self.offering.price = item[4]

    def add_to_cart(self):
        self.cart.items.append(self.offering)
        exit_screen(self.add_item_screen)

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
