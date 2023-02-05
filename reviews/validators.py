from django.core.exceptions import ValidationError
import re

phone_re = re.compile('\+375\s\(29|33|44|25\)\s\d{3}\-\d{2}\-\d{2}')


def validate_phone_number(value):
    """validates that a value is a phone number"""
    if phone_re.match(value) is None:
        raise ValidationError("Неверный формат телефонного номера")
