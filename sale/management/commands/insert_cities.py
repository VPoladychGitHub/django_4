import random
from django.core.management.base import BaseCommand, CommandError
from sale.models import City


class Command(BaseCommand):
    help = 'set in parameter count of add cities'

    def add_arguments(self, parser):
        parser.add_argument('sale_city', nargs='+', type=int)

    def handle(self, *args, **options):
        len_insert = options['sale_city'][0]

        if len_insert < 1:
            raise CommandError(f'argument = {len_insert} not in diapason: more then 1')
        else:
            ps = self.cities(len_insert)
            for p_in in ps:
                p = City(name=p_in[0], number_inhabitants=p_in[1])
                p.save(force_insert=True)
                self.stdout.write(self.style.SUCCESS(f'City: {p} '))

            self.stdout.write(self.style.SUCCESS(f'Success insert {len_insert} City'))

    @staticmethod
    def cities(ln):
        return_arr: list = list()
        for i in range(ln):
            r_l = random.randint(5, 8)
            cityname = ''
            for j in range(r_l):
                cityname += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

            populations = random.randint(500, 1300)
            return_arr.append((cityname + 'XXX', populations))
        return return_arr
