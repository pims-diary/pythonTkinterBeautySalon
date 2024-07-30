from tkinter import *
from tkinter import ttk

screen = Tk()

my_weekdays_names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]


def weekday_selection(event):
    for x in range(7):
        if weekdaysDropdown.get() == my_weekdays_names[x]:
            print(my_weekdays_names[x])


weekdaysDropdown = ttk.Combobox(screen, values=my_weekdays_names)
weekdaysDropdown.current(1)
# weekdaysDropdown.bind("<<ComboboxSelected>>", weekday_selection)
weekdaysDropdown.grid()
