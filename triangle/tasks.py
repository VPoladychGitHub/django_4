from celery import shared_task
from django.core.mail import send_mail as django_send_mail
import requests
from triangle.models import AutherQuote
from bs4 import BeautifulSoup


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


@shared_task
def parse_quoters():
    r = requests.get('https://quotes.toscrape.com/')
    html_soup = BeautifulSoup(r.text, 'html.parser')
    aq = html_soup.find_all('div', class_='quote')
    print(type(aq))
    print(len(aq))
    ind: int = 0
    for a in aq:
        quote = a.find('span', class_='text').text
        aouth = a.find(class_="author").text
        q_serch = quote[1:8]
        res_aquote = ""
        try:
            res_aquote = AutherQuote.objects.get(quote__contains=q_serch)
        except Exception:
            pass
        if not res_aquote:
            print(f"aouth: {aouth}: quote: {quote}")
            p = AutherQuote(name=aouth, quote=quote)
            p.save()
            print(quote)
            print(aouth)
            ind += 1
            if ind >= 5:
                break

    if ind == 0:
        send_mail_homework.delay('no quotes', "больше нет цитат ", ["home@test.com"])
