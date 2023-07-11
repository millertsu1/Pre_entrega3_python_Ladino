from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/',verbose_name='Book Image', null=True)
    description = models.TextField(null=True, verbose_name='Description')

    def __str__(self):
        row = "Title: " + self.title + " - " + "Description: " + self.description
        return row
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/',verbose_name='Course Image', null=True)
    description = models.TextField(null=True, verbose_name='Description')
    
    def __str__(self):
        row2 = "Title: " + self.title + " - " + "Description: " + self.description
        return row2

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile' )#related_name='profile'
    image = models.ImageField(upload_to='avatares', null = True, blank=True)












