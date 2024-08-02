from Data.DataLink.SqlDatabaseToData import validate_user
from Resources.Common.Reuse import is_textfield_empty


def login(username, password):
    """Handle the login logic
        validating the username and password"""
    return validate_user(username, password)
