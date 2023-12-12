import datetime
import json
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers
from uploadbook.forms import BookForm
from book.models import Book
from uploadbook.models import UploadBook
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
@csrf_exempt
def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:account'))
    
    context = {'form': form}
    return render(request, "add_book.html", context)

@login_required
@csrf_exempt
def edit_book(request, id):
    item = UploadBook.objects.get(pk = id)
    form = BookForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:account'))

    context = {'form': form}
    return render(request, "edit_book.html", context)

@csrf_exempt
def delete_book(request, id):
    # Dapatkan data buku berdasarkan ID
    book = UploadBook.objects.get(pk=id)
    
    if request.method == "POST":
        # Hapus data buku dari database
        book.delete()
        return HttpResponseRedirect(reverse('main:account'))
    
    return render(request, "confirmation_template.html", {'book': book})

@login_required
@csrf_exempt
def tambah_stocks(request, book_id):
    data = get_object_or_404(Book, pk=id)
    
    data.stocks += 1
    data.save()
    
    return HttpResponseRedirect(reverse('main:account'))

@login_required
@csrf_exempt
def kurang_stocks(request, book_id):
    data = get_object_or_404(Book, pk=id)
    
    if data.stock > 0:
        data.stock -= 1
        data.save()
    
    return HttpResponseRedirect(reverse('main:account'))
    
@csrf_exempt
def get_book_json(request):
    product_item = UploadBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        isbn = request.POST.get("isbn")
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")
        publisher = request.POST.get("publisher")
        image = request.POST.get("image")
        price = request.POST.get("price")
        stocks = request.POST.get("stocks")
        user = request.user

        new_book = Book(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image=image, price=price, stocks=stocks)
        new_book.save()
        upload_book = UploadBook(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image=image, price=price, stocks=stocks, user=user)
        upload_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_book_ajax(request, id):
    if request.method == 'POST':
        try:
            data = UploadBook.objects.get(id=id)
            data.delete()
            return HttpResponse("OK", status=200)
        except Book.DoesNotExist:
            return HttpResponse("Buku tidak ada", status=404)

    return HttpResponseNotFound()

@login_required
@csrf_exempt
def upload_book_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            isbn = data.get("isbn")
            title = data.get("title")
            author = data.get("author")
            year = data.get("year")
            publisher = data.get("publisher")
            image = data.get("image")
            price = data.get("price")
            stocks = data.get("stocks")
            user = request.user

            new_book = Book.objects.create(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image=image, price=price, stocks=stocks)
            new_book.save()
            upload_book = UploadBook.objects.create(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image=image, price=price, stocks=stocks, user=user)
            upload_book.save()

            return JsonResponse({"status": "success"}, status=201)
        except KeyError:
            return JsonResponse({"status": "error", "message": "Invalid data provided"}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request"}, status=401)