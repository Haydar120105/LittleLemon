from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemview
from restaurant.serializers import MenuSerializer

class MenuItemviewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title='Test Menu 1', price=1, inventory=1)
        self.menu2 = Menu.objects.create(title='Test Menu 2', price=2, inventory=2)
        

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(len(serializer.data), 2)
        self.assertEqual(serializer.data[0]['title'], self.menu1.title)
        self.assertEqual(serializer.data[1]['title'], self.menu2.title)
