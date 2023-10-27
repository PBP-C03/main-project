from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Nota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)