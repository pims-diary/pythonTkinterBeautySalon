import tkinter as tk

from Data.DataLink.SqlDatabaseToData import validate_user
from Resources.Common.Reuse import custom_messagebox, validate_fields
from Pages.Navigation.PageNavigation import navigate_to, Feature


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("600x400")
        self.root.configure(bg="white")
        self.username_entry = None
        self.password_entry = None
        self.user_data = None

        self.render_login_screen()

    def render_login_screen(self):
        # Title label
        title_label = tk.Label(self.root, text="STAFF LOGIN", font=("Times", 20, "bold"), bg="white", fg="#333333")
        title_label.pack(pady=30)

        # Username label and entry
        username_label = tk.Label(self.root, text="Username", font=("Times", 18, "bold"), bg="white", fg="#333333")
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.username_entry.pack(pady=7)

        # Password label and entry
        password_label = tk.Label(self.root, text="Password", font=("Times", 18, "bold"), bg="white", fg="#333333")
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*", font=("Helvetica", 10))
        self.password_entry.pack(pady=7)

        # Login button
        login_button = tk.Button(self.root, text="Login", font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                 command=self.login)
        login_button.pack(pady=50)

    def login(self):
        """Handle the login logic
            validating the username and password"""

        # Check for empty text fields
        if not validate_fields((self.username_entry, self.password_entry)):
            custom_messagebox("Blank Field Error", "Cannot leave username or password field blank", "error")
            return

        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        # Check username and password exist in database
        login_result = validate_user(entered_username, entered_password)

        if login_result:
            # Navigate to Home page
            navigate_to(Feature.HOME, self.root)
        else:
            custom_messagebox("Invalid Credentials Error", "Invalid username or password", "error")
            return
