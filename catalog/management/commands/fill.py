import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Здесь мы получаем данные из фикстуры с категориями"""
        with open("fixtures/catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
            category_data = []
            for item in data:
                if item["model"] == "catalog.category":
                    category_data.append(item)

        return category_data

    @staticmethod
    def json_read_products():
        """Здесь мы получаем данные из фикстуры с продуктами"""
        with open("fixtures/catalog_data.json", encoding="utf-8") as file:
            data = json.load(file)
            product_data = []
            for item in data:
                if item["model"] == "catalog.product":
                    product_data.append(item)

        return product_data

    def handle(self, *args, **options):
        Product.objects.all().delete()  # Удалите все продукты
        Category.objects.all().delete()  # Удалите все категории

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category["pk"],
                         name=category["fields"]["name"],
                         description=category["fields"]["description"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product["pk"],
                        name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price_per_purchase=product["fields"]["price_per_purchase"],
                        created_at=product["fields"]["created_at"]
                        )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
