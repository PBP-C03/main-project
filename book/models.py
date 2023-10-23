from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stocks = models.IntegerField(blank=True, null=True)