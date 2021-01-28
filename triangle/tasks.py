from celery import shared_task
from django.core.mail import send_mail as django_send_mail


@shared_task
def send_mail_homework(subject, message, email):
    print(f"message: {message} :{email} ")
    django_send_mail(subject, message, 'admin@example.com', [email])


#  django_send_mail("subject", message, ['admin@example.com'], email)


@shared_task
def add(x, y):
    print(x + y)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_mail_django_(subject, message, from_email):
    django_send_mail(subject, message, from_email, ['admin@example.com'])


@shared_task
def send_mail_to_admin():
    django_send_mail("subject", "message", 'test@test.com', ['admin@example.com'])
