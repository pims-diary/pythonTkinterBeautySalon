import tkinter as tk
from tkinter.ttk import Notebook
from Data.Models.Cart import Cart
from Resources.Common.Reuse import destroy_child_view


class PaymentMethod:
    def __init__(self, root, cart: Cart):
        self.root = root
        self.cart = cart

        # Frames
        self.order_summary_frame = None
        self.payment_frame = None
        self.tab_control = None

        self.render_page()

    def render_page(self):
        title_label = tk.Label(self.root, text="Order Summary", font=("Helvetica", 18, "bold"), bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        self.order_summary_frame = tk.Frame(self.root)
        self.order_summary_frame.pack()

        title_label = tk.Label(self.root, text="Pay by: ", font=("Helvetica", 14, "bold"), bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        self.payment_frame = tk.Frame(self.root)
        self.payment_frame.pack(fill=tk.BOTH)

        self.render_order_summary()
        self.render_payment_section()

    def render_order_summary(self):
        destroy_child_view(self.order_summary_frame)

        height = len(self.cart.items)
        for i in range(height):
            tk.Label(self.order_summary_frame, text=self.cart.items[i].offering.name).grid(row=i, column=0)
            tk.Label(self.order_summary_frame, text="$" + str(self.cart.items[i].offering.price)).grid(row=i, column=1)
            tk.Label(self.order_summary_frame, text=self.cart.items[i].no_of_items).grid(row=i, column=3)
            if self.cart.items[i].discount == 0.0:
                discount = 'N/A'
            else:
                discount = self.cart.items[i].discount
            tk.Label(self.order_summary_frame, text=discount).grid(row=i, column=4)
            tk.Label(self.order_summary_frame, text="$" + str(self.cart.items[i].total_price)).grid(row=i, column=5)

        tk.Label(self.order_summary_frame, text="Gift: ").grid(row=height + 1, column=0)
        if self.cart.customer.is_new:
            gift = "20.00"
        else:
            gift = "0.00"
        tk.Label(self.order_summary_frame, text="$" + str(gift)).grid(row=height + 1, column=2)

        tk.Label(self.order_summary_frame, text="Total Amount: ").grid(row=height + 2, column=0)
        tk.Label(self.order_summary_frame, text="$" + str(self.cart.total_amount)).grid(row=height + 2, column=2)

    def render_payment_section(self):
        self.tab_control = Notebook(self.payment_frame)

        # create a number of tabs you want to add
        tab1 = tk.Frame(self.tab_control, width=600, height=280)
        tab2 = tk.Frame(self.tab_control, width=600, height=280)

        # add the tabs to the tabcontrol
        self.tab_control.add(tab1, text='Credit Card')
        self.tab_control.add(tab2, text='Cash Payment')

        # grid the tabcontrol
        self.tab_control.pack(fill=tk.BOTH)

        tk.Label(tab1, text="Tab 1").pack()
        tk.Label(tab2, text="Tab 2").pack()
