from django.shortcuts import render
from book.models import Book
from main.models import Profile
from cartbook.models import Cart,Book_Cart
from checkoutbook.models import Nota
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.

def display_order(request):
    cart = Cart.objects.get(user=request.user)
    book_cart = Book_Cart.objects.filter(carts = cart)
    context = {
        'cart':cart,
        'book_carts' : book_cart
    }
    return render(request,'checkout.html',context)

def get_nota(request):
    if request.method == 'GET':
        nota = Nota.objects.filter(user=request.user)
        print(serialize('json', nota))
        return HttpResponse(serialize('json', nota))
    return HttpResponseNotFound()

@csrf_exempt
def pay_order(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user = request.user)
        cart = Cart.objects.get(user = request.user)
        if profile.saldo >= cart.total_harga:
            nota = Nota(user = request.user, total_amount = cart.total_amount, total_harga = cart.total_harga)
            nota.save()
            orders = Book_Cart.objects.filter(carts = cart)
            for order in orders.iterator():
                order.book.stocks -= order.amount
                order.nota = nota
                order.save()

            profile.saldo -= cart.total_harga
            profile.save()

            cart.delete()
            new_cart = Cart(user = request.user)
            new_cart.save()
            return HttpResponse(b"SUCCESS",status=201)
        return HttpResponseBadRequest(b"FAILED")

    return HttpResponseNotFound()
