from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    review = models.TextField()
