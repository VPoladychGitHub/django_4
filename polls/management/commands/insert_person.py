import random
from django.core.management.base import BaseCommand, CommandError
from polls.models import Person


class Command(BaseCommand):
    help = 'insert person'

    def add_arguments(self, parser):
        parser.add_argument('poll_person', nargs='+', type=int)

    def handle(self, *args, **options):
        len_insert = options['poll_person'][0]

        if len_insert > 10 or len_insert < 1:
            raise CommandError(f'argument = {len_insert} not in diapason: less 10 and more then 1')
        else:
            ps = self.persons(len_insert)
            for p_in in ps:
                p = Person(username=p_in[0], email=p_in[1], password=p_in[2])
                p.save(force_insert=True)
                self.stdout.write(self.style.SUCCESS(f'Person: {p} '))

            self.stdout.write(self.style.SUCCESS(f'Success insert {len_insert} Person'))

    @staticmethod
    def persons(ln):
        return_arr: list = list()
        for i in range(ln):
            r_l = random.randint(5, 8)
            username = ''
            for j in range(r_l):
                username += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            email_user = username + '@user.com'
            pass_l = random.randint(5, 13)
            password = ''
            for j in range(pass_l):
                password += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_123456789')

            return_arr.append((username, email_user, password))
        return return_arr
