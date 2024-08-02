import tkinter as tk


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
