from urllib.request import urlopen

from celery import shared_task
from django.core.mail import send_mail as django_send_mail
import requests
from triangle.models import Auther, Quote
from bs4 import BeautifulSoup


@shared_task
def send_mail_homework(subject, message, email):
    print(f"message: {message} :{email} ")
    django_send_mail(subject, message, 'admin@example.com', [email])


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


@shared_task
def parse_quoters():
    i: int = 1
    ind: int = 0
    while True:
        url = f'https://quotes.toscrape.com/page/{i}/'
        try:
            page = urlopen(url)
        except Exception:
            print("page = urlopen(url)")
            break
        soup = BeautifulSoup(page, 'html.parser')
        aq = soup.find_all('div', class_='quote')
        for a in aq:
            quote = a.find('span', class_='text').text
            author = a.find(class_="author").text
            # print(f"quote: {quote}  author: {author} ")
            res_aquote = ""
            try:
                res_aquote = Quote.objects.get(quote__contains=quote)
            except Exception:
                pass
            if not res_aquote:
                try:
                    obj, created = Auther.objects.get_or_create(name=author)
                except Exception as ss:
                    print(ss)
                try:
                    obj_aquote, created_aquote = Quote.objects.get_or_create(auther=obj, quote=quote)
                    ind += 1
                except Exception as ss22:
                    print(ss22)
                if ind >= 5:
                    break
        if ind >= 5:
            break
        i += 1

    if ind < 5:
        send_mail_homework.delay('no quotes', "больше нет цитат ", ["home@test.com"])
