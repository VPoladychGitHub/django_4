from datetime import datetime
from datetime import timedelta
import pytz
from django import forms
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from triangle.models import Auther, Contact, Quote
from django_4 import settings


class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['from_email', 'subject', 'message', 'result']


class AutherForm(forms.ModelForm):
    class Meta:
        model = Auther
        fields = ['name']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'auther']


class EmailForm(forms.Form):
    # send_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    send_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS)
    send_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_send_date(self):
        send_date = self.cleaned_data['send_date']
        print(send_date)
        today = datetime.utcnow()
        date_max = today + timedelta(days=2)
        d1 = pytz.utc.localize(today)
        d2 = pytz.utc.localize(date_max)
        dt = send_date + timedelta(microseconds=-1)
        if dt > d2 or dt < d1:
            value = dt
            raise ValidationError(_('Invalid  diapason date, dt: %(value)s'),
                                  code='invalid',
                                  params={'value': value}, )

        return send_date


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
