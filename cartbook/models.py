from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from checkoutbook.models import Nota

# Create your models here.
class Cart (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField(default=0)
    total_harga = models.IntegerField(default=0)

# # Buat Objek baru dalam bentuk Book
class Book_Cart (models.Model): # Untuk Setiap Buku
    amount = models.IntegerField(default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # Banyak Buku bisa diletakkan di 1 CART User
    carts = models.ForeignKey(Cart, on_delete=models.SET_NULL, null= True) # Setiap Buku bisa dimiliki oleh banyak CART
    subtotal = models.IntegerField(default=0)
    notes = models.TextField(default="",blank=True, null=True)
    nota = models.ForeignKey(Nota, null= True,blank=True,on_delete= models.CASCADE) #Menghubungkan Buku yang dipesan ke dalam nota
