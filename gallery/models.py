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

    





