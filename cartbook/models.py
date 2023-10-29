from django.db import models
<<<<<<< HEAD
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Cart (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField(default=0)
    total_harga = models.IntegerField(default=0)


# # Buat Objek baru dalam bentuk Book
class Book_Cart (models.Model): # Untuk Setiap Buku
    amount = models.IntegerField(default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # Banyak Buku bisa diletakkan di 1 CART User
    carts = models.ForeignKey(Cart, on_delete=models.CASCADE) # Setiap Buku bisa dimiliki oleh banyak CART
    subtotal = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
=======

# Create your models here.
>>>>>>> 4642e5a548e37da44d751325c4bdfa27fd39b267
