from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=10)
    title = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stocks = models.IntegerField(blank=True, null=True)