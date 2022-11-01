from tabnanny import verbose
from django.db import models

# Create your models here.

class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    ISBN=models.CharField(max_length=100, verbose_name='ISBN')
    title=models.CharField(max_length=100, verbose_name='Book')
    images=models.ImageField(upload_to='imagenes/', verbose_name="Images",  null=True)
    description=models.TextField(verbose_name="Description", max_length=500)

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100, verbose_name='Username')
    ISBN=models.CharField(max_length=100, verbose_name='ISBN')
    Review=models.CharField(max_length=100, verbose_name='Comment')