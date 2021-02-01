import math
import pytz

from django.contrib import messages
from django.core.exceptions import ValidationError
from pipenv.vendor.importlib_resources._py3 import _

from triangle.forms import ContactFrom, EmailForm, TriangleForm
from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail
from triangle.tasks import send_mail_django_, send_mail_homework

def send_email_form(request):
    if request.method == "GET":
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            send_email = form.cleaned_data['send_email']
            message = form.cleaned_data['message']
            send_date = form.cleaned_data['send_date']
            # today = datetime.datetime.utcnow()
            # date_max = today + datetime.timedelta(days=2)
            # d1 = pytz.utc.localize(today)
            # d2 = pytz.utc.localize(date_max)
            # dt = send_date + datetime.timedelta(microseconds=-1)
            # if dt > d2 or dt < d1:
            #     messages.add_message(request, messages.ERROR, 'Message not sent')
            #     value = dt
            #     raise ValidationError(_('Invalid  diapason date, dt: %(value)s'),
            #                           code='invalid',
            #                           params={'value': value}, )
            # else:
            send_mail_homework.apply_async(('subject', message, [send_email]), eta=send_date)
                # send_mail_homework.delay('subject', message, [send_email])
                # send_mail('subject', message, 'admin@example.com', [send_email])
                # send_mail_homework.apply_async(('subject', message,  [send_email]), eta=dt)

            messages.add_message(request, messages.SUCCESS, 'Message sent')
            return redirect('send_email')

    return render(
        request,
        "triangle/contact.html",
        context={
            "form": form,
        }
    )


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
            send_mail_django_.delay(subject, message, from_email)
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
