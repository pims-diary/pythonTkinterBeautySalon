import tkinter as tk


class PopUpForm:
    """Class for creating forms for different menu options.
        Demonstrates inheritance."""

    def __init__(self, root):
        """Initialize the form window"""
        self.new_window = tk.Toplevel(root)
        self.new_window.configure(bg="#add8e6")
        self.main_frame = None

        self.render_main_form()

    def render_main_form(self):
        self.main_frame = tk.Frame(self.new_window, bg="#add8e6")
