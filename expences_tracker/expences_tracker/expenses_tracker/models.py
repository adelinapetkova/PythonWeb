from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from expences_tracker.expenses_tracker.validators import only_letters_validator, min_length_name_validator


@deconstructible
class MaxFileSizeInMBValidator:
    def __init__(self, max_size):
        self.max_size=max_size

    def __call__(self, value):
        filesize=value.file.size
        if filesize>self.max_size*1024*1024:
            raise ValidationError(f'Max file size is {self.max_size:.2f} MB')


class Profile(models.Model):
    NAME_MAX_LENGTH=15
    IMAGE_MAX_SIZE_IN_MB=5
    IMAGE_UPLOAD_TO_DIR='profiles/'

    first_name=models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            only_letters_validator,
            min_length_name_validator,
            # MinLengthValidator
        ),
    )

    last_name=models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            only_letters_validator,
            min_length_name_validator,
        ),
    )

    budget=models.FloatField(
        default=0,
        validators=(
            MinValueValidator(0),
        ),
    )

    profile_image=models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMBValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )


class Expense(models.Model):
    TITLE_MAX_LENGTH=30

    title=models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image=models.URLField()

    description=models.TextField(
        null=True,
        blank=True,
    )

    price=models.FloatField()



