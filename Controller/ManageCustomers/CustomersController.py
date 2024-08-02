from Resources.Common.Reuse import is_textfield_empty
from Data.DataLink.SqlDatabaseToData import create_customer, get_last_customer_id
from Data.Models.Customer import Customer


def generate_customer_id():
    current_last_id = get_last_customer_id()
    current_last_id = current_last_id + 1
    return current_last_id


def perform_add_customer(customer: Customer):
    customer_id = generate_customer_id()
    create_customer(customer_id, customer)
