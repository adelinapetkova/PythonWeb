from django.db import models


class Profile(models.Model):
    MAX_LEN_FIRST_NAME=30
    MAX_LEN_LAST_NAME=30

    first_name=models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
    )

    last_name=models.CharField(
        max_length=MAX_LEN_LAST_NAME,
    )

    image_url=models.URLField()


class Book(models.Model):
    MAX_LEN_TITLE=30
    MAX_LEN_TYPE=30

    title=models.CharField(
        max_length=MAX_LEN_TITLE,
    )

    description=models.TextField()

    image=models.URLField()

    type=models.CharField(
        max_length=MAX_LEN_TYPE,
    )



