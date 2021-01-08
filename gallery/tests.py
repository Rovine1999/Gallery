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
        self.assertTrue(len(image_test) >0)

    def test_save_method(self):
        self.image_test.delete_image()
        image_test=Image.objects.all()
        self.assertTrue(len(image_test)== 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.new_image.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)


