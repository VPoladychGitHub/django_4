from django import forms
from person.models import Person


class PersonalModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', "email"]
