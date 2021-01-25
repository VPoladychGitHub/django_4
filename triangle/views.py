import math
from django.contrib import messages
from django.core.exceptions import ValidationError
from pipenv.vendor.importlib_resources._py3 import _

from triangle.forms import ContactFrom, TriangleForm
from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail
from triangle.tasks import send_mail as celary_send_mail

def triangle_form(request):
    diagonal: str = str()
    if request.method == "GET":
        diagonal = None
        form = TriangleForm()
    else:
        form = TriangleForm(request.POST)
        if form.is_valid():
            catet_1 = form.cleaned_data['catet_1']
            catet_2 = form.cleaned_data['catet_2']
            if catet_1 < 0 or catet_2 < 0:
                if catet_1 < 0:
                    value = catet_1
                else:
                    value = catet_2
                raise ValidationError(_('Invalid value < 0: %(value)s'),
                                      code='invalid',
                                      params={'value': value}, )
            diagonal = str(math.sqrt(catet_1 ** 2 + catet_2 ** 2))
            # return redirect('triangle')
    # print(f"diagonal3333:  {diagonal}")
    return render(
        request,
        "triangle/triangle.html",
        context={
            "form": form,
            "diagonal": diagonal
        }
    )


def contact_form(request):
    if request.method == "GET":
        form = ContactFrom()
    else:
        form = ContactFrom(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            celary_send_mail(subject, message, from_email)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
            try:
                print(f"subject: {subject}  from_email: {from_email} message:  {message}")
                # send_mail(subject, message, from_email, ['admin@example.com'])
                # messages.add_message(request, messages.SUCCESS, 'Message sent')
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'Message not sent')
            return redirect('contact')
    return render(
        request,
        "triangle/contact.html",
        context={
            "form": form,
        }
    )
