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
from .forms import NotaForm
# Create your views here.

def get_order(request):
    if request.method == 'GET':
        cart = Cart.objects.get(user=request.user)
        book_cart = Book_Cart.objects.filter(carts = cart)
        return HttpResponse(serialize('json', book_cart))
    return HttpResponseNotFound()

def display_order(request):
    cart = Cart.objects.get(user=request.user)
    book_cart = Book_Cart.objects.filter(carts = cart)
    form = NotaForm()
    context = {
        'cart':cart,
        'book_carts' : book_cart,
        'form':form
    }
    return render(request,'checkout.html',context)

def get_nota(request):
    if request.method == 'GET':
        nota = Nota.objects.filter(user=request.user)
        return HttpResponse(serialize('json', nota))
    return HttpResponseNotFound()

def pay_order(request):
    form = NotaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        profile = Profile.objects.get(user = request.user)
        cart = Cart.objects.get(user = request.user)
        print(request.POST)
        alamat = request.POST.get("Alamat")
        metode = request.POST.get("Metode")
        if profile.saldo >= cart.total_harga:
            nota = Nota(user = request.user, total_amount = cart.total_amount, total_harga = cart.total_harga, alamat = alamat, metode = metode)
            nota.save()
            orders = Book_Cart.objects.filter(carts = cart)
            for order in orders.iterator():
                order.book.stocks -= order.amount
                order.nota = nota
                order.save()

            profile.saldo -= cart.total_harga
            profile.save()
            print(serialize('json', [nota]))
            cart.delete()
            new_cart = Cart(user = request.user)
            new_cart.save()
            
            return HttpResponse(b"SUCCESS",status=201)
        return HttpResponseBadRequest(b"FAILED")

    return HttpResponseNotFound()
