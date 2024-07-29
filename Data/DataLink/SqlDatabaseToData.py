import pyodbc

connection_string = ("Driver={ODBC Driver 17 for SQL Server};"
                     "Server=20220661-PRIYAN;"
                     "Database=BeautySalon;"
                     "Trusted_Connection=yes;")

connection = pyodbc.connect(connection_string)


def print_users():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users")
    for row in cursor.fetchall():
        print(row)


def validate_user(username, password):
    cursor = connection.cursor()

    query = '''
    SELECT * FROM Users WHERE username = ? AND password = ?
    '''

    cursor.execute(query, (username, password))

    if len(cursor.fetchall()) != 0:
        return True
    else:
        return False
