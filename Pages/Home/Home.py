import tkinter as tk
from PIL import ImageTk, Image
from Pages.ParentPages.MainMenu import MainMenu


class Home(MainMenu):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Home")
        self.root.geometry("600x400")

    def render_page_contents(self):
        self.menu_label = tk.Label(self.root, text="Welcome to the Beauty Hub Salon", font=("Helvetica", 18, "bold"),
                                   bg="#add8e6", fg="#333333")
        self.menu_label.pack(pady=30)

        c = tk.Canvas(self.root, width=600, height=150)
        c.pack()

        img = ImageTk.PhotoImage(Image.open(r"Resources/Images/salon_welcome.png"))
        print("welcome")
        c.create_image(10, 10, image=img, anchor=tk.NW)
