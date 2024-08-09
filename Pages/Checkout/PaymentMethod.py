import tkinter as tk
from tkinter.ttk import Notebook
from Controller.Checkout.CheckoutController import insert_new_bill, calculate_balance
from Data.Models.Cart import Cart
from Resources.Common.Rules import Discounts
from Resources.Common.Reuse import destroy_child_view, exit_screen, custom_messagebox
from Pages.ParentPages.PopUpForm import PopUpForm
from Pages.Navigation.PageNavigation import navigate_to, Feature


class PaymentMethod(PopUpForm):
    def __init__(self, root, cart: Cart):
        super().__init__(root)
        self.root = root
        self.payment_window = self.new_window
        self.payment_window.geometry("600x500")
        self.cart = cart

        # Frames
        self.order_summary_frame = None
        self.payment_frame = None
        self.tab_control = None
        self.tab_credit_card = None
        self.tab_cash = None
        self.balance_frame = None

        # Entries
        self.card_number_entry = None
        self.card_name_entry = None
        self.card_expiry_entry = None
        self.card_cvv_entry = None
        self.cash_by_customer = None

        # Labels
        self.balance_display = None

        self.render_page()

    def render_page(self):
        title_label = tk.Label(self.payment_window, text="Order Summary", font=("Helvetica", 18, "bold"), bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        self.order_summary_frame = tk.Frame(self.payment_window)
        self.order_summary_frame.pack()

        title_label = tk.Label(self.payment_window, text="Pay by: ", font=("Helvetica", 14, "bold"), bg="#add8e6",
                               fg="#333333")
        title_label.pack(pady=30)

        self.payment_frame = tk.Frame(self.payment_window)
        self.payment_frame.pack(fill=tk.BOTH)

        self.render_order_summary()
        self.render_payment_section()

    def render_order_summary(self):
        destroy_child_view(self.order_summary_frame)

        height = len(self.cart.items)
        # Control structure: Looping implementation
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
            self.cart.gift = Discounts.NEW_CUSTOMER_GIFT_AMOUNT
        else:
            gift = "0.00"
            self.cart.gift = Discounts.OLD_CUSTOMER_GIFT_AMOUNT

        tk.Label(self.order_summary_frame, text="$" + str(gift)).grid(row=height + 1, column=2)

        tk.Label(self.order_summary_frame, text="Total Amount: ").grid(row=height + 2, column=0)
        tk.Label(self.order_summary_frame, text="$" + str(self.cart.total_amount)).grid(row=height + 2, column=2)

    def render_payment_section(self):
        self.tab_control = Notebook(self.payment_frame)

        # create a number of tabs you want to add
        self.tab_credit_card = tk.Frame(self.tab_control, width=600, height=280)
        self.tab_cash = tk.Frame(self.tab_control, width=600, height=280)

        # add the tabs to the tabcontrol
        self.tab_control.add(self.tab_credit_card, text='Credit Card')
        self.tab_control.add(self.tab_cash, text='Cash Payment')

        # grid the tabcontrol
        self.tab_control.pack(fill=tk.BOTH)

        self.render_credit_card_tab_details()
        self.render_cash_tab_details()

    def render_credit_card_tab_details(self):
        card_fields_frame = tk.Frame(self.tab_credit_card)
        card_fields_frame.pack()
        tk.Label(card_fields_frame, text="Card number").grid(row=0, column=0)
        self.card_number_entry = tk.Entry(card_fields_frame)
        self.card_number_entry.grid(row=0, column=1)

        tk.Label(card_fields_frame, text="Name on card").grid(row=1, column=0)
        self.card_name_entry = tk.Entry(card_fields_frame)
        self.card_name_entry.grid(row=1, column=1)

        tk.Label(card_fields_frame, text="Expiry date").grid(row=2, column=0)
        self.card_expiry_entry = tk.Entry(card_fields_frame)
        self.card_expiry_entry.grid(row=2, column=1)

        tk.Label(card_fields_frame, text="CVV").grid(row=3, column=0)
        self.card_cvv_entry = tk.Entry(card_fields_frame)
        self.card_cvv_entry.grid(row=3, column=1)

        tk.Button(self.tab_credit_card, text="COMPLETE PAYMENT", command=self.complete_payment).pack()

    def render_cash_tab_details(self):
        cash_fields_frame = tk.Frame(self.tab_cash)
        cash_fields_frame.pack()

        tk.Label(cash_fields_frame, text="How much cash in NZD did the customer offer?").pack()
        self.cash_by_customer = tk.Entry(cash_fields_frame)
        self.cash_by_customer.pack(pady=7)
        tk.Button(cash_fields_frame, text="Check Balance", command=self.check_balance_amount).pack()
        self.balance_frame = tk.Frame(cash_fields_frame)
        self.balance_frame.pack()

    def check_balance_amount(self):
        try:
            cash_amount = float(self.cash_by_customer.get())
        except ValueError:
            custom_messagebox("Invalid Input", "Please provide a monetory amount", "error")
            return

        destroy_child_view(self.balance_frame)
        balance_amount = calculate_balance(cash_amount, self.cart.total_amount)
        if balance_amount == 0.0:
            tk.Label(self.balance_frame,
                     text="No balance is owed. Click on the button below to complete payment.").pack()
            tk.Button(self.balance_frame, text="COMPLETE PAYMENT", command=self.complete_payment).pack()
        elif balance_amount > 0.0:
            tk.Label(self.balance_frame, text="Please return $" + str(balance_amount) + " to the customer, and then "
                                                                                        "click on the button below to "
                                                                                        "complete payment").pack()
            tk.Button(self.balance_frame, text="COMPLETE PAYMENT", command=self.complete_payment).pack()
        else:
            tk.Label(self.balance_frame,
                     text="The customer needs to pay $" + str(balance_amount)[
                                                          1:] + " more to complete payment. ").pack()

            tk.Label(self.balance_frame,
                     text="Fill in the new full amount paid by the customer above and click on Check Balance button "
                          "again to continue.").pack()

    def complete_payment(self):
        if len(self.card_number_entry.get()) == 0:
            payment_method = "Cash"
        else:
            payment_method = self.card_number_entry.get()
        # Data structure: Tuple returned by the function
        result = insert_new_bill(payment_method, self.cart)

        # Data structure: Tuple - Value used from tuple
        is_success = result[0]
        if is_success:
            exit_screen(self.payment_window)
            navigate_to(Feature.HOME, self.root)
            custom_messagebox("Payment Complete!", "The order has been completed.\nORDER NUMBER: " + str(result[1]), "info")
        else:
            custom_messagebox("Payment Failed", "There was an error in the Order Payment", "error")
