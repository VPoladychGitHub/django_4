from django.core.management.base import BaseCommand
from polls.models import Person  #


class Command(BaseCommand):
    help = 'set in parameter count of add users'

    def add_arguments(self, parser):
        parser.add_argument('poll_person', nargs='+', type=int)

    def handle(self, *args, **options):
        len_insert = options
        p = Person(username="Bruce", email="Bruse@test.com", password="12345")
        p.save(force_insert=True)

        self.stdout.write(self.style.SUCCESS(f'Success insert {len_insert}'))
