from django import forms
from django.forms import ModelForm

from person.models import MyModel, Person


class PersonalModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', "email"]


class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['color']