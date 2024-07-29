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


def load_customer_data():
    """Read the stored user data from a text file"""
    customer_data = {}  # dictionary to store user data
    index = 1

    try:
        with open('customer.txt', 'r') as file:
            for line in file:
                customerId, name, email, phone, type = line.strip().split(',')
                # Using dictionary to store user credentials
                customer_data[index] = {
                    'customerId': customerId,
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'type': type
                }
                index = index + 1

    except FileNotFoundError:
        messagebox.showerror("Error", "User data file not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    return customer_data
