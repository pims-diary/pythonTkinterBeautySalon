import tkinter as tk
from tkinter import messagebox


def load_user_data():
    """Read the stored user data from a text file"""
    user_data = {}  # dictionary to store user data

    try:
        with open('login.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                user_data[username] = password  # Using dictionary to store user credentials
    except FileNotFoundError:
        messagebox.showerror("Error", "User data file not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    return user_data


def custom_messagebox(title, message, msg_type):
    """Show customized message boxes"""
    if msg_type == "info":
        messagebox.showinfo(title, message)
    elif msg_type == "error":
        messagebox.showerror(title, message)


class LoginApplication:
    def __init__(self, root):
        """Initialize the main login application"""
        self.menu_label = None
        self.file_menu = None
        self.menu_bar = None
        self.menu_frame = None
        self.root = root
        self.root.title("Login System")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        # Title label
        self.title_label = tk.Label(self.root, text="STAFF LOGIN", font=("Times", 20, "bold"), bg="white", fg="#333333")
        self.title_label.pack(pady=30)

        # Username label and entry
        self.username_label = tk.Label(self.root, text="Username", font=("Times", 18, "bold"), bg="white", fg="#333333")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.username_entry.pack(pady=7)

        # Password label and entry
        self.password_label = tk.Label(self.root, text="Password", font=("Times", 18, "bold"), bg="white", fg="#333333")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*", font=("Helvetica", 10))
        self.password_entry.pack(pady=7)

        # Login button
        self.login_button = tk.Button(self.root, text="Login", font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                      command=self.login)
        self.login_button.pack(pady=50)

        # Load user data from text file
        self.user_data = load_user_data()

    def login(self):
        """Handle the login logic
            validating the username and password"""
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username in self.user_data and self.user_data[entered_username] == entered_password:
            # self.custom_messagebox("Success", "Login successful!", "info")
            self.show_main_menu()
        else:
            custom_messagebox("Error", "Invalid username or password", "error")

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


# Create the main window
rt = tk.Tk()
app = LoginApplication(rt)

# Run the main event loop
rt.mainloop()