from django.db import models

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



class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    user_type = models.CharField(max_length=50, verbose_name='User type')
    phone_number = models.CharField(max_length=20,verbose_name='Phone Number')

    """ def __str__(self):
        return self.name """
    
    def __str__(self):
        row1 = "Name: " + self.name + " - " + "User Type: " + self.user_type
        return row1


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/',verbose_name='Course Image', null=True)
    description = models.TextField(null=True, verbose_name='Description')
    
    def __str__(self):
        row2 = "Title: " + self.title + " - " + "Description: " + self.description
        return row2

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank=True)











