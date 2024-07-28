import tkinter as tk
from Resources.Data import Data
from Resources.Common import Reuse
from Pages.MainMenu.MainMenu import MainMenu


class Login:
    def __init__(self, root):
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
        self.user_data = Data.load_user_data()

    def login(self):
        """Handle the login logic
            validating the username and password"""
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username in self.user_data and self.user_data[entered_username] == entered_password:
            menu = MainMenu(self.root)
            menu.show_main_menu()
        else:
            Reuse.custom_messagebox("Error", "Invalid username or password", "error")

