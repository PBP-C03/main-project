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
@login_required
def get_desc(request,id):
    if request.method == 'GET':
        nota = Nota.objects.get(pk = id)
        books = []
        order = Book_Cart.objects.filter(nota = nota)
        for item in order:
            books.append(Book.objects.get(pk = item.pk))
        print(serialize('json', books))
        return HttpResponse(serialize('json', books))
    return HttpResponseNotFound() 
@login_required
def get_order(request):
    if request.method == 'GET':
        cart = Cart.objects.get(user=request.user)
        book_cart = Book_Cart.objects.filter(carts = cart)
        return HttpResponse(serialize('json', book_cart))
    return HttpResponseNotFound()
@login_required
def get_book(request,id):
    if request.method == 'GET':
        book = Book.objects.get(pk = id)
        print(serialize('json', [book]))
        return HttpResponse(serialize('json', [book]))
    return HttpResponseNotFound()
@login_required
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
@login_required
def get_nota(request):
    if request.method == 'GET':
        nota = Nota.objects.filter(user=request.user).order_by('pk') 
        return HttpResponse(serialize('json', nota))
    return HttpResponseNotFound()

@csrf_exempt
def del_nota(request,id):
    if request.method == 'POST':
        nota = Nota.objects.filter(user=request.user)
        nota_del = nota.get(pk = id)
        nota_del.delete()
        return HttpResponse(b"SUCCESS",status=201)
    return HttpResponseBadRequest(b"FAILED")
@login_required
def pay_order(request):
    form = NotaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        profile = Profile.objects.get(user = request.user)
        cart = Cart.objects.get(user = request.user)
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
            cart.delete()
            new_cart = Cart(user = request.user)
            new_cart.save()
            
            return HttpResponse(b"SUCCESS",status=201)
        return HttpResponseBadRequest(b"FAILED")

    return HttpResponseNotFound()

@login_required
@csrf_exempt
def inc_book(request,id):
    if request.method == 'POST':
        cart = Cart.objects.get(user = request.user)
        order = Book_Cart.objects.filter(carts = cart)
        book = order.get(book = id)
        book.amount+=1
        book.save()
        return HttpResponse(b"SUCCESS",status=201)
    return HttpResponseBadRequest(b"FAILED")

@login_required
@csrf_exempt
def dec_book(request,id):
    if request.method == 'POST':
        cart = Cart.objects.get(user = request.user)
        order = Book_Cart.objects.filter(carts = cart)
        book = order.get(book = id)
        book.amount-=1
        book.save()
        return HttpResponse(b"SUCCESS",status=201)
    return HttpResponseBadRequest(b"FAILED")

@login_required
@csrf_exempt
def del_book(request,id):
    if request.method == 'POST':
        cart = Cart.objects.get(user = request.user)
        order = Book_Cart.objects.filter(carts = cart)
        book = order.get(book = id)
        book.delete()
        return HttpResponse(b"SUCCESS",status=201)
    return HttpResponseBadRequest(b"FAILED")
