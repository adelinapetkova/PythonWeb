from django import forms

from library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'image_url':forms.URLInput(attrs={'placeholder': 'URL'}),
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image':forms.URLInput(attrs={'placeholder': 'Image'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction,Novel,Crime...'}),
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required=False

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    class Meta:
        model=Profile
        fields='__all__'
