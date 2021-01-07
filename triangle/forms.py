from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class TriangleFormRes(forms.Form):
    diagonal = forms.IntegerField()


class TriangleForm(forms.Form):
    catet_1 = forms.IntegerField(required=True)
    catet_2 = forms.IntegerField(required=True)

    # def clean_catet_1(self):
    #     data = self.cleaned_data['catet_1']
    #     print(data)
    #     if data < 0:
    #         raise ValidationError(_('Invalid data < 0'))



class ContactFrom(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_subject(self):
        data = self.cleaned_data['subject']
        if len(data) < 2:
            raise ValidationError(_('Invalid data < 2'))
