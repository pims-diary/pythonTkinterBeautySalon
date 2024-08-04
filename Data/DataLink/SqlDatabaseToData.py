import pyodbc
from Data.Models.Customer import Customer
from Data.Models.Bill import Bill
from Data.Models.Cart import Cart, CartItem

connection_string = ("Driver={ODBC Driver 17 for SQL Server};"
                     "Server=20220661-PRIYAN;"
                     "Database=BeautySalon;"
                     "Trusted_Connection=yes;")

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


def print_users():
    cursor.execute("SELECT * FROM Users")
    for row in cursor.fetchall():
        print(row)


def validate_user(username, password):
    query = '''
    SELECT * FROM Users WHERE username = ? AND password = ?
    '''

    cursor.execute(query, (username, password))

    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False


def create_customer(customer_id: int, customer: Customer):
    is_success = False
    try:
        query = '''
        INSERT INTO Customers(customerId, name, email, phone, type, isNew)
        VALUES (?, ?, ?, ?, ?, ?)
        '''

        cursor.execute(query,
                       (customer_id, customer.name, customer.email, customer.phone, customer.type, customer.is_new))

        connection.commit()
        is_success = True

    except pyodbc.Error as e:
        print("Error: ", e)
        is_success = False
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
        return is_success


def get_last_customer_id():
    query = '''
        SELECT customerId FROM Customers WHERE customerId=(SELECT max(customerId) FROM Customers)
        '''

    cursor.execute(query)

    customer_id: int = cursor.fetchall()[0][0]

    return customer_id


def get_last_customer():
    query = '''
        SELECT * FROM Customers WHERE customerId=(SELECT max(customerId) FROM Customers)
        '''

    cursor.execute(query)
    customer_info = cursor.fetchall()

    customer = Customer()
    customer.id = customer_info[0][0]
    customer.name = customer_info[0][1]
    customer.email = customer_info[0][2]
    customer.phone = customer_info[0][3]
    customer.type = customer_info[0][4]
    customer.is_new = customer_info[0][5]

    return customer


def search_customer(customer_id):
    query = '''
        SELECT * FROM Customers WHERE customerId=?
        '''

    cursor.execute(query, customer_id)

    return cursor.fetchall()


def search_offering(offering_id):
    query = '''
        SELECT * FROM Offerings WHERE offeringId=?
        '''

    cursor.execute(query, offering_id)

    return cursor.fetchall()


def create_bill(bill: Bill):
    is_success = False
    try:
        query = '''
        INSERT INTO Bills(billId, customerId, customerEmail, paymentDetails, orders)
        VALUES (?, ?, ?, ?, ?)
        '''

        orders = create_orders_string(bill.cart)

        cursor.execute(query,
                       (bill.bill_id, bill.customer_id, bill.customer_email, bill.payment_details, orders))

        connection.commit()
        is_success = True

    except pyodbc.Error as e:
        print("Error: ", e)
        is_success = False
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
        return is_success


def get_last_bill_id():
    query = '''
        SELECT billId FROM Bills WHERE billId=(SELECT max(billId) FROM Bills)
        '''

    cursor.execute(query)

    bill_id: int = cursor.fetchall()[0][0]

    return bill_id


def create_orders_string(cart: Cart):
    cart_items: list[CartItem] = cart.items
    items_str = ""
    for item in cart_items:
        items_str = items_str + (";item;"
                                 + str(item.offering.id) + ";"
                                 + item.offering.name + ";"
                                 + item.offering.type + ";"
                                 + item.offering.description + ";"
                                 + item.offering.price + ";"
                                 + str(item.no_of_items) + ";"
                                 + str(item.discount) + ";"
                                 + str(item.total_price)
                                 + ";item;")
    customer_str = (";cust;"
                    + str(cart.customer.id) + ";"
                    + cart.customer.name + ";"
                    + cart.customer.email + ";"
                    + cart.customer.phone + ";"
                    + cart.customer.type + ";"
                    + str(cart.customer.is_new)
                    + ";cust;")

    orders: str = (";items;" + items_str + ";items;"
                   + customer_str
                   + ";total;" + str(cart.total_amount) + ";total;"
                   + ";gift;" + str(cart.gift) + ";gift;")
    return orders


def create_cart_object_from_db_string(orders: str):
    cart = Cart()
    cart_item = CartItem()

    # Separate the string into strings for items, customer, total amount and gift
    items_str = orders.split(";items;")[0]
    customer_str = orders.split(";customer;")[1]
    total_amount_str = orders.split(";total;")[1]
    gift_str = orders.split(";gift;")[1]

    # Separate each offering item into a string and put them in a list
    item_str_list = items_str.split(";item;")

    # Add each offering into cart as each item along with the number of items and the discount on them
    for item_str in item_str_list:
        if len(item_str) == 0:
            continue
        else:
            item_properties = item_str.split(";")
            cart_item.offering.id = int(item_properties[0])
            cart_item.offering.name = item_properties[1]
            cart_item.offering.type = item_properties[2]
            cart_item.offering.description = item_properties[3]
            cart_item.offering.price = item_properties[4]
            cart_item.no_of_items = int(item_properties[5])
            cart_item.discount = float(item_properties[6])

            cart.items.append(cart_item)

    # Add details of the associated customer within the cart
    customer_properties = customer_str.split(";")
    cart.customer.id = int(customer_properties[0])
    cart.customer.name = customer_properties[1]
    cart.customer.email = customer_properties[2]
    cart.customer.phone = customer_properties[3]
    cart.customer.type = customer_properties[4]
    cart.customer.is_new = True if customer_properties[5] == "True" else False

    # Add the total amount and the gift to the cart
    cart.total_amount = float(total_amount_str)
    cart.gift = float(gift_str)

    return cart


# Sample
# string = ";item;My Item;item;;item;My Other Item;item;;item;My Third Item;item;;item;My Last Item;item;"
#
# array = string.split(";item;")
#
# for item in array:
#     print(item)
