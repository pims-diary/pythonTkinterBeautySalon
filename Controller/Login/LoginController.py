from Data.DataLink.SqlDatabaseToData import validate_user
from Resources.Common.Reuse import is_textfield_empty


def login(username, password):
    """Handle the login logic
        validating the username and password"""
    return validate_user(username, password)


def validate_fields(username_field, password_field):
    if is_textfield_empty(username_field) or is_textfield_empty(password_field):
        return False
    return True
