from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='New York')
        self.location.save_location()

        self.category = Category(name='Home')
        self.category.save_category()

        self.image_test = Image(id=1, name='photo', description='photo test', location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_method(self)
    
