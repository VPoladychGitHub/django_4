from django import forms
from sale.models import City


class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'number_inhabitants']
