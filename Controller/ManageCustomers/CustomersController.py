from Resources.Common.Reuse import is_textfield_empty


def validate_fields(name_field, email_field, phone_field):
    if (
            is_textfield_empty(name_field) or
            is_textfield_empty(email_field) or
            is_textfield_empty(phone_field)
    ):
        return False
    return True
