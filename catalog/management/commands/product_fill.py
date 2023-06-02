from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    """Класс который, удаляет товары из базы данных, потом его заполняет"""

    def handle(self, *args, **options):
        Product.objects.all().delete()  # object deleted товары из базы данных

        product_list = [

                    {'name': 'ЗЕРНОСУШИЛКА',
                     'description': 'Работают на природном и сжиженном газе.',
                     "image": '',
                     'category': 'сельхоз',
                     'price': 3000000, 'creation_at': '2023-06-02', 'modified_at': '2023-06-02'},

                    {'name': 'Машина первичной чистки зерна',
                    'description': 'Предназначаются для очистки вороха зерновых и бобовых культур. ',
                    'image': '',
                    'category': 'сельхоз',
                    'price': '5000000',
                    'creation_at': '2023-06-02',
                    'modified_at': '2023-06-02'},

                    {'name': 'Норийная вышка',
                     'description': 'Нории предназначены для вертикального перемещения зернового вороха.',
                     'image': '',
                     'category': 'сельхоз',
                     'price': '6000000',
                     'creation_at': '2023-06-02',
                     'modified_at': '2023-06-02'},

                    {'name': 'силос',
                     'description': 'Современный вариант хранения зерна с сохранением всех полезных свойств',
                     'image': '',
                     'category': 'сельхоз',
                     'price': '9000000',
                     'creation_at': '2023-06-02',
                     'modified_at': '2023-06-02'}


        ]

        products_objects = []
        for product_item in product_list:
            products_objects.append(Product(**product_item))

        Product.objects.bulk_create(products_objects)
