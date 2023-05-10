from django.core.management.base import BaseCommand

from factories import ProductFactory


class Command(BaseCommand):
    help = 'Generate products'

    def handle(self, *args, **options):
        ProductFactory.create_batch(size=10000)
        self.stdout.write(self.style.SUCCESS('Successfully generated products.'))
