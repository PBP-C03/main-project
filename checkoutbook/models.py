from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Nota(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateField(default=timezone.now())
    total_amount = models.IntegerField()
    total_harga = models.IntegerField()