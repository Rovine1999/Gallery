from django.db import models
import datetime as dt


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)



    def save_location(self):
        self.save()


    def delete_location(self):
        self.delete()


    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
    
    def __str__(self):
     return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=50):

    



class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)


    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()


    