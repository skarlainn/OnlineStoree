from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the database from fixture"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "products_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))