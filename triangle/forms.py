from django import forms


class TriangleFormRes(forms.Form):
    diagonal = forms.IntegerField()


class TriangleForm(forms.Form):
    catet_1 = forms.IntegerField(required=True)
    catet_2 = forms.IntegerField(required=True)
  #  diagonal = forms.CharField(required=False)


class ContactFrom(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

