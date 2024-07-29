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


def create_customer(customer_id, customer: Customer):
    try:
        query = '''
        INSERT INTO Customers(customerId, name, email, phone, type)
        VALUES (?, ?, ?, ?, ?)
        '''

        cursor.execute(query, (customer_id, customer.name, customer.email, customer.phone, customer.type))

        connection.commit()

    except pyodbc.Error as e:
        print("Error: ", e)
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()
