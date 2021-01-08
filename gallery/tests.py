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

    def test_save_method(self):
        self.image_test.save_image()
        image_test=Image.objects.all()
        self.assertTrue(len(image_test) > 0)

    def test_delete_method(self):
        self.image_test.delete_image()
        image_test=Image.objects.all()
        self.assertTrue(len(image_test)== 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos')
        image_test = Image.objects.filter(image='photos')
        self.assertTrue(len(image_test) == 0)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(id=1,name='Nairobi')


    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))


    def test_save_method(self):
        self.location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location) > 0)    
        

    def test_delete_method(self):
        self.location.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location)== 0)

    def test_update_location(self):
        self.location.update_location(id=id, value=value)
        self.location.update_location(self.location.id, 'value')
        location = Location.objects.filter(location='value')
        self.assertTrue(len(location) == 0)

class TestCategory(TestCase):
    def setUp():
        self.category = Category(id=1,name='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.location.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category) > 0) 


    def test_delete_method(self):
        self.category.delete_category()
        category=Category.objects.all()
        self.assertTrue(len(category)== 0)

       