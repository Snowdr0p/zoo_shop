from django.core.exceptions import ValidationError
import re


def validate_phone_number(value: str):
    """validates that a value is a phone number"""
    phone_re = re.compile('\+375\s?\(?(29|44|33|25)\)?(\s|-)?\d{3}(\s|-)?\d{2}(\s|-)?\d{2}')
    digits_re = re.compile('\d')
    if len(digits_re.findall(value)) != 12 or phone_re.match(value) is None:
        raise ValidationError("Неверный формат телефонного номера")
