import tkinter as tk
from Pages.MainMenu.Toolbar import Toolbar


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.menu_frame = None
        self.menu_label = None

    def show_main_menu(self):
        """Display the main menu / dashboard after successful login"""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.menu_frame = tk.Frame(self.root, bg="#add8e6")
        self.menu_frame.pack(fill=tk.BOTH, expand=True)

        tools = Toolbar(self.root)
        tools.render_toolbar()

        self.menu_label = tk.Label(self.menu_frame, text="Welcome to the Main Menu", font=("Helvetica", 18, "bold"),
                                   bg="#add8e6", fg="#333333")
        self.menu_label.pack(pady=30)
