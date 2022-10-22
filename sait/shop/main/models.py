from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptoin = models.TextField()
    price = models.FloatField()
    category_id = models.IntegerField()

class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200)
# Create your models here.
