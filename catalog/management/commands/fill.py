from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {"title": "Смартфон", "pk": 1},
            {"title": "Ноутбук", "pk": 2},
            {"title": "Видеокарта", "pk": 3}
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(Category(**category))

        Category.objects.bulk_create(categories_for_create)

        product_list = [
            {"title": "iphone 14", "pk": 1, "category": Category.objects.get(pk=1), "purchase_price": 89000},
            {"title": "iphone 12", "pk": 2, "category": Category.objects.get(pk=1), "purchase_price": 69000},
            {"title": "samsung galaxy s23 ultra", "pk": 3, "category": Category.objects.get(pk=1), "purchase_price": 110000},
            {"title": "Apple MacBook Pro", "pk": 4, "category": Category.objects.get(pk=2), "purchase_price": 105000},
            {"title": "Acer Nitro 5", "pk": 5, "category": Category.objects.get(pk=2), "purchase_price": 96000},
            {"title": "MSI Bravo 15", "pk": 6, "category": Category.objects.get(pk=2), "purchase_price": 99000},
            {"title": "GIGABYTE GeForce RTX 4090", "pk": 7, "category": Category.objects.get(pk=3), "purchase_price": 204000},
            {"title": "Radeon pro w7800", "pk": 8, "category": Category.objects.get(pk=3), "purchase_price": 219000},
        ]

        products_for_create = []
        for product in product_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)
