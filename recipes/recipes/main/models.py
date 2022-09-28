from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 30
    INGREDIENTS_MAX_LENGTH = 250

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image_url = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LENGTH,
        null=True,
        blank=True
    )

    time = models.IntegerField()


