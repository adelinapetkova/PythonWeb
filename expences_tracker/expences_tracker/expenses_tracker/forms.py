from django import forms

from expences_tracker.expenses_tracker.models import Profile


class CreateProfileForm(forms.Form):
    budget = forms.FloatField(
        min_value=0,
    )

    first_name = forms.CharField(
        max_length=15,
    )

    last_name = forms.CharField(
        max_length=15,
    )

    profile_image = forms.ImageField(
        required=False,
    )


class CreateEditExpenseForm(forms.Form):
    title=forms.CharField(
        max_length=30,
    )

    description=forms.CharField(
        widget=forms.Textarea,
        required=False,
    )

    expense_image=forms.URLField()

    price=forms.FloatField(
        min_value=0,
    )


class DeleteExpenseForm(forms.Form):
    title=forms.CharField(
        disabled=True,
    )

    description=forms.CharField(
        widget=forms.Textarea,
        disabled=True,
    )

    expense_image=forms.URLField(
        disabled=True,
    )

    price=forms.FloatField(
        disabled=True,
    )


class EditProfileForm(forms.Form):
    budget=forms.FloatField(
        min_value=0,
    )

    first_name=forms.CharField(
        max_length=15,
        min_length=2,
    )

    last_name = forms.CharField(
        max_length=15,
        min_length=2,
    )

    profile_image = forms.ImageField(
        required=False,
    )
