from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, Book_Cart
from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from cartbook.forms import NoteForm

from django.http import JsonResponse

# Create your views here.
@login_required
@csrf_exempt
def view_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    book_carts = Book_Cart.objects.filter(carts=user_cart)

    # Filter Buku by Title Book di CART
    search_query = request.GET.get('search', '')
    if search_query:
        book_carts = Book_Cart.objects.filter(carts=user_cart, book__title__icontains=search_query)
    else:
        book_carts = Book_Cart.objects.filter(carts=user_cart)
    
    total_amount = user_cart.total_amount
    total_harga = 0

    for book_cart in book_carts:
        # Hitung subtotal untuk setiap item dalam keranjang
        subtotal = book_cart.book.price * book_cart.amount
        book_cart.subtotal = subtotal  # Simpan subtotal ke dalam model
        book_cart.save()
        total_harga += subtotal

    user_cart.total_harga = total_harga  # Update total_harga pada keranjang
    user_cart.save()

    context = {
        'book_carts': book_carts,
        'total_amount': total_amount,
        'total_harga': total_harga,
        'note_form': NoteForm(),
    }

    return render(request, 'cartbook.html', context)

@login_required
@csrf_exempt
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


    return redirect('cartbook:view_cart')

@login_required
@csrf_exempt
def remove_from_cart(request, book_cart_id):
    try:
        book_cart = Book_Cart.objects.get(id=book_cart_id)
        user_cart = book_cart.carts
        user_cart.total_amount -= book_cart.amount
        user_cart.total_harga -= (book_cart.book.price * book_cart.amount)
        user_cart.save()
        book_cart.delete()

        return JsonResponse({'success': True, 'total_harga': user_cart.total_harga})
    except Book_Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

@login_required
@csrf_exempt
def tambah_amount(request, book_cart_id):
    book_cart = Book_Cart.objects.get(id=book_cart_id)
    user_cart = book_cart.carts
    book_cart.amount += 1
    book_cart.subtotal += book_cart.book.price
    book_cart.save()
    user_cart.total_harga += book_cart.book.price
    user_cart.save()
    return JsonResponse({'success': True, 'amount': book_cart.amount, 'subtotal': book_cart.subtotal, 'total_harga': user_cart.total_harga})

@login_required
@csrf_exempt
def kurang_amount(request, book_cart_id):
    book_cart = Book_Cart.objects.get(id=book_cart_id)
    user_cart = book_cart.carts
    if book_cart.amount > 0:
        book_cart.amount -= 1
        book_cart.subtotal -= book_cart.book.price
        user_cart.total_harga -= book_cart.book.price
        book_cart.save()
        user_cart.save()
    if book_cart.amount == 0:
        book_cart.delete()
        return JsonResponse({'success': True, 'amount': book_cart.amount, 'subtotal': book_cart.subtotal, 'total_harga': user_cart.total_harga, 'deleted': True})
    return JsonResponse({'success': True, 'amount': book_cart.amount, 'subtotal': book_cart.subtotal, 'total_harga': user_cart.total_harga, 'deleted': False})


@login_required
@csrf_exempt
def add_note(request, book_cart_id):
    try:
        book_cart = Book_Cart.objects.get(id=book_cart_id)
        form = NoteForm(request.POST, instance=book_cart)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'note': form.cleaned_data['notes']})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid form'}, status=400)
    except Book_Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)




