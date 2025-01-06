from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="test menu",
            price=10.99,
            inventory=5
        )
        self.assertEqual(item, "test menu : 10.99 : 5")