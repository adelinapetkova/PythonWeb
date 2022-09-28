from django import forms
from django.core.exceptions import ValidationError


def ingredients_validator(value):
    if " " in value:
        raise ValidationError("Ingredients must be separated only by comma!")


class RecipeCreateForm(forms.Form):
    title = forms.CharField(
        max_length=30,
    )

    image_url = forms.URLField(
        label='Image URL'
    )

    description = forms.CharField(widget=forms.Textarea)

    ingredients = forms.CharField(
        max_length=250,
        validators=(
            ingredients_validator,
        )
    )

    time = forms.IntegerField(
        label='Time(Minutes)'
    )


class RecipeEditForm(forms.Form):
    title = forms.CharField(
        max_length=30,
    )

    image_url = forms.URLField(
        label='Image URL'
    )

    description = forms.CharField(widget=forms.Textarea)

    ingredients = forms.CharField(
        max_length=250,
        validators=(
        )
    )

    time = forms.IntegerField(
        label='Time(Minutes)'
    )


class RecipeDeleteForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        disabled=True,
    )

    image_url = forms.URLField(
        label='Image URL',
        disabled=True,
    )

    description = forms.CharField(
        widget=forms.Textarea,
        disabled=True,
    )

    ingredients = forms.CharField(
        max_length=250,
        disabled=True,
        validators=(
            ingredients_validator,
        )
    )

    time = forms.IntegerField(
        label='Time(Minutes)',
        disabled=True,
    )

