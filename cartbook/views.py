from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cart, Book_Cart
from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    book_carts = Book_Cart.objects.filter(carts=user_cart)
    
    total_amount = user_cart.total_amount
    total_harga = 0  # Inisialisasi total harga dengan 0
    subtotal = 0


    for book_cart in book_carts:
        # Hitung subtotal untuk setiap item dalam keranjang
        subtotal = book_cart.book.price * book_cart.amount
        total_harga += subtotal  # Tambahkan ke total harga

    context = {
        'book_carts': book_carts,
        'total_amount': total_amount,
        'total_harga': total_harga,
        'subtotal': subtotal,
    }

    return render(request, 'cartbook.html', context)

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Cari buku dalam keranjang
    book_cart, created = Book_Cart.objects.get_or_create(book=book, carts=user_cart)

    if created:
        # Jika buku belum ada di keranjang, tambahkan dengan amount 1
        book_cart.amount = 1
        book_cart.save()
    else:
        # Jika buku sudah ada di keranjang, tambahkan amount dengan 1
        book_cart.amount += 1
        book_cart.save()

    # Update total amount dan total harga pada keranjang
    user_cart.total_amount += 1
    user_cart.total_harga += book.price
    user_cart.save()

    # messages.success(request, f'{book.title} added to your cart.')

    return redirect('cartbook:view_cart')


@login_required
def remove_from_cart(request, book_cart_id):
    book_cart = Book_Cart.objects.get(id=book_cart_id)
    user_cart = book_cart.carts
    user_cart.total_amount -= book_cart.amount
    user_cart.total_harga -= (book_cart.book.price * book_cart.amount)
    user_cart.save()
    
    book_cart.delete()

    messages.success(request, 'Book removed from your cart.')

    return redirect('cartbook:view_cart')

def hilang (request):
    Cart.objects.all().delete()
    return HttpResponse("haii")