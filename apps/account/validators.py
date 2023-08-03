import re
from email.utils import parseaddr

from django.forms import ValidationError


def validate_email_address(email_address: str) -> tuple[bool, str]:
    """
    Validate if given email is valid or not.

    Args:
        email_address (str): given email address

    Raises:
        ValidationError: given string doesn't contains a valid email address

    Returns:
        tuple[bool, str]: if found returns true with email address else false
    """

    is_valid: bool = True
    valid_email_address:str = ""

    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not email_pattern.match(email_address):
        is_valid = False
    else:
        _, valid_email_address = parseaddr(email_address)
        if not valid_email_address:
            is_valid = False

    if not is_valid:
        raise ValidationError(
            ("%(value)s is not a valid email address"),
            params={"value": email_address},
        )
    return is_valid, valid_email_address
