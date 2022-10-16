import json
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """
    Класс пополнения базы данных
    информацией по продуктам.
    """

    def handle(self, *args, **options):
        with open('data/ingredients.json', 'rb') as f:
            data = json.load(f)
            for i in data:
                obj, created = Ingredient.objects.get_or_create(name=i['name'],
                                                                measurement_unit=i['measurement_unit'])
                print(obj, created)
