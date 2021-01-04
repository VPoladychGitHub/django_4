import math
from django.contrib import messages
from triangle.forms import TriangleForm, ContactFrom, TriangleFormRes
from django.shortcuts import redirect, render
from django.core.mail import BadHeaderError, send_mail


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
            diagonal = str(math.sqrt(int(catet_1) ** 2 + int(catet_2) ** 2))
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
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
                messages.add_message(request, messages.SUCCESS, 'Message sent')
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
