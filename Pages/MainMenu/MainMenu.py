import tkinter as tk


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.menu_label = None
        self.file_menu = None
        self.menu_bar = None
        self.menu_frame = None

    def show_main_menu(self):
        """Display the main menu / dashboard after successful login"""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.menu_frame = tk.Frame(self.root, bg="#add8e6")
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)

        # Add options to the file menu
        self.file_menu.add_command(label="Manage Customer", command=self.manage_customer)
        self.file_menu.add_command(label="Services", command=self.services)
        self.file_menu.add_command(label="Products", command=self.products)
        self.file_menu.add_command(label="Members", command=self.members)
        self.file_menu.add_command(label="Billing", command=self.billing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.menu_label = tk.Label(self.menu_frame, text="Welcome to the Main Menu", font=("Helvetica", 18, "bold"),
                                   bg="#add8e6", fg="#333333")
        self.menu_label.pack(pady=30)

    def manage_customer(self):
        """Open Manage Customer form"""
        Form(self.root, "Manage Customer")

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


class Form:
    """Class for creating forms for different menu options.
        Demonstrates inheritance."""

    def __init__(self, root, title):
        """Initialize the form window"""
        self.new_window = tk.Toplevel(root)
        self.new_window.title(title)
        self.new_window.geometry("600x500")
        self.new_window.configure(bg="white")

        self.title_label = tk.Label(self.new_window, text=title, font=("Helvetica", 18, "bold"), bg="#add8e6",
                                    fg="#333333")
        self.title_label.pack(pady=30)

        # Example label for the form
        self.example_label = tk.Label(self.new_window, text=f"This is the {title} form.", font=("Helvetica", 14),
                                      bg="#add8e6", fg="#333333")
        self.example_label.pack(pady=20)
