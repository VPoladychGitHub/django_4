from celery import shared_task
from django.core.mail import send_mail as django_send_mail

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
def send_mail(subject, message,from_email):
    django_send_mail(subject, message, from_email, ['admin@example.com'])
