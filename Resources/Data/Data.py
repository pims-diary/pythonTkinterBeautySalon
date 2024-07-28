from tkinter import messagebox


def load_user_data():
    """Read the stored user data from a text file"""
    user_data = {}  # dictionary to store user data

    try:
        with open('login.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                user_data[username] = password  # Using dictionary to store user credentials
    except FileNotFoundError:
        messagebox.showerror("Error", "User data file not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    return user_data
