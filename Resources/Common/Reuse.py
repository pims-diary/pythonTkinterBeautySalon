from Resources.Common.Root import root
from tkinter import messagebox


def destroy_child_view(master):
    """ Destroys all child widgets of master """
    for i in master.winfo_children():
        i.destroy()


def exit_app():
    """ Terminate the App """
    root.destroy()


def custom_messagebox(title, message, msg_type):
    """Show customized message boxes"""
    if msg_type == "info":
        messagebox.showinfo(title, message)
    elif msg_type == "error":
        messagebox.showerror(title, message)


def is_textfield_empty(textfield):
    return True if len(textfield.get()) == 0 else False


def combo_selection(combo_box, combo_list):
    for x in range(len(combo_list)):
        if combo_box.get() == combo_list[x]:
            return combo_list[x]
