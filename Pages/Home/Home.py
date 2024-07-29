import tkinter as tk
from Pages.MainMenu.MainMenu import MainMenu


class Home(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Home")
        self.root.geometry("600x400")

    def render_home_page(self):
        self.menu_label = tk.Label(self.menu_frame, text="Welcome to the Main Menu", font=("Helvetica", 18, "bold"),
                                   bg="#add8e6", fg="#333333")
        self.menu_label.pack(pady=30)
