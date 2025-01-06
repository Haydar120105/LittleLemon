from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="test menu",
            price=10.99,
            inventory=5
        )
        self.assertEqual(item.title == "test menu", True)
        self.assertEqual(item.price == 10.99, True)
        self.assertEqual(item.inventory == 5, True)