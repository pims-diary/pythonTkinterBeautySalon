from tkinter import messagebox
import tkinter as tk


def destroy_child_view(widget):
    """ Destroys all child widgets of master """
    if widget is not None:
        for i in widget.winfo_children():
            i.destroy()


def clean_master_view(master):
    """ Destroys all child widgets of master """
    destroy_child_view(master)
    master.geometry("600x400")


def exit_screen(master):
    """ Terminate the Screen """
    if master is not None:
        master.destroy()


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


def validate_fields(fields: tuple):
    for field in fields:
        if is_textfield_empty(field):
            return False
    return True


def single_row_table(parent, items, column_names):
    if len(items) == len(column_names):
        for i in range(len(column_names)):
            tk.Label(parent, text=column_names[i], font='Helvetica 10 bold').grid(row=0, column=i)
            tk.Label(parent, text=items[i]).grid(row=1, column=i)


def single_column_table(parent, items: list, row_names: list):
    if len(items) == len(row_names):
        for i in range(len(row_names)):
            tk.Label(parent, text=row_names[i], font='Helvetica 10 bold').grid(row=i, column=0)
            tk.Label(parent, text=items[i]).grid(row=i, column=1)


def pack_all(widget):
    for c in widget.children:
        widget.children[c].pack()
