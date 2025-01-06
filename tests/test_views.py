from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemview
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient

class MenuItemviewTest(TestCase):
    def setup(self):
        self.menu1 = Menu.objects.create(name='Test Menu 1', description='Test Menu 1 Description')
        self.menu2 = Menu.objects.create(name='Test Menu 2', description='Test Menu 2 Description')
        self.menu3 = Menu.objects.create(name='Test Menu 3', description='Test Menu 3 Description')

    
    def test_getall(self):
        client = APIClient()
        response = client.get('/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items)
        self.assertEqual(response.data, serializer.data)
