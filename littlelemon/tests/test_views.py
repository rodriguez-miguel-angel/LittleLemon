from django.urls import reverse

from django.shortcuts import get_object_or_404

from django.test import TestCase, Client
from rest_framework.test import APIClient


from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from restaurant.models import Menu, Booking
from restaurant.serializers import MenuItemSerializer, BookingSerializer
from restaurant.views import MenuItemsView

import json

class MenuViewTest(TestCase):
    
    """
    Use the setup() method to add a few test instances of the Menu model.
    """
    def setUp(self):
        # See <https://www.django-rest-framework.org/api-guide/testing/>.
        
        user = User.objects.create(username='test_user')
        user.set_password('test_password')
        user.save()

        Token.objects.create(user=user)

        # Include an appropriate `Authorization:` header on all requests.
        token = Token.objects.get(user__username='test_user')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        Menu.objects.create(title="44 oz Tomahawk Steak", price=121.00, inventory=10)
        Menu.objects.create(title="16 oz Ribeye Steak", price=22.00, inventory=10)
        Menu.objects.create(title="12 oz NY Prime Steak", price=18.00, inventory=10)


    def test_menu_db(self):
        items = Menu.objects.all()    
        self.assertEqual(len(items), 3)

    """
    Add another test_getall() instance method to retrieve all the Menu objects added for the test purpose. 
    The retrieved objects must serialized, 
    so make sure the method runs assertions to check if the serialized data equals the response.
    """
    def test_getall(self):
        """
        version-01:
        url = "http://127.0.0.1:8000/restaurant/menu/"
        version-02:
        """
        url = reverse('menu')
        response = self.client.get(url)
        json_response = json.loads(response.content)

        items = Menu.objects.all()
        serialized_item = MenuItemSerializer(items, many=True)
        results = serialized_item.data
        
        """
        version-a:
        for idx, item in enumerate(json_response):
            self.assertEqual(items[idx].title, item["title"])
            self.assertEqual(str(items[idx].price), item["price"])
            self.assertEqual(items[idx].inventory, item["inventory"])
        """
        """
        version-b:
        """
        for idx, item in enumerate(json_response):
            self.assertEqual(results[idx]['title'], item["title"])
            self.assertEqual(results[idx]['price'], item["price"])
            self.assertEqual(results[idx]['inventory'], item["inventory"])
        self.assertEqual(len(items), len(json_response))
    


    # See <https://stackoverflow.com/questions/49206514/what-is-the-best-way-to-test-modules-in-views>.
    def test_menu_view_list(self):
        """
        version-01:
        url = "http://127.0.0.1:8000/restaurant/menu/"
        version-02:
        """
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
