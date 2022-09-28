from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


def min_length_name_validator(value):
    if len(value)<2:
        raise ValidationError('Ensure length is greater than 2.')
