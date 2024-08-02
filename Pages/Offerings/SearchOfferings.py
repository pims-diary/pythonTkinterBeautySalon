import tkinter as tk


class SearchOfferings:
    def __init__(self):
        self.root = tk.Frame


    def render_offerings_form(self):
        # search product / services form
        search_label = tk.Label(self.root, text="Search a product or service:")
        search_label.pack(pady=10)
        self.search_entry = tk.Entry(frame, font=("Helvetica", 10))
        self.search_entry.pack(pady=7)

        page = SearchOfferings(frame)
        search_button = tk.Button(frame, font=("Times", 16, "bold"), bg="#4caf50", fg="#ffffff",
                                  command=page.search)

    def search(self):
        pass
