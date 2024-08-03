import pyodbc
from Data.Models.Customer import Customer

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
