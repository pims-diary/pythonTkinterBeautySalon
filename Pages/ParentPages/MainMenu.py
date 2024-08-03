import tkinter as tk
from Pages.ParentPages.Toolbar import Toolbar
from Resources.Common.Reuse import clean_master_view


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#add8e6")
        self.menu_frame = None
        self.menu_label = None
        self.show_main_menu()

    def show_main_menu(self):
        """Display the main menu / dashboard after successful login"""
        clean_master_view(self.root)

        self.menu_frame = tk.Frame(self.root, bg="#add8e6")

        tools = Toolbar(self.root)
        tools.render_toolbar()
