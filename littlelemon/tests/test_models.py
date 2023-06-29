from django.test import TestCase

from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    
    def instance(self):
        new_instance = Menu(title="44 oz Tomahawk Steak", price=121.00, inventory=10)
        return new_instance
    
    def test_menu_instance(self):
        item = self.instance()
        # self.assertEqual(str(item), "[[Menu]] title: 44 oz Tomahawk Steak. price: 121.00. inventory: 10.")
        self.assertEqual(str(item), "[[Menu]] title: 44 oz Tomahawk Steak. price: 121.0. inventory: 10.")

    """
    Call the assertEqual() method of the test class that 
    compares the string representation of the newly added object with the anticipated value.
    """
    def test_get_item(self):
        item = Menu.objects.create(title="44 oz Tomahawk Steak", price=121.00, inventory=10)
        # self.assertEqual(str(item), "[[Menu]] title: 44 oz Tomahawk Steak. price: 121.00. inventory: 10.")
        self.assertEqual(str(item), "[[Menu]] title: 44 oz Tomahawk Steak. price: 121.0. inventory: 10.")