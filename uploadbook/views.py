import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, Http404
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
def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:account'))
    
    context = {'form': form}
    return render(request, "add_book.html", context)

def edit_book(request, id):
    item = UploadBook.objects.get(pk = id)
    form = BookForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:account'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

@login_required
def delete_book(request, book_id):
    try:
        book = UploadBook.objects.get(id=book_id)
        book.delete()

        return JsonResponse({'success': True})
    except UploadBook.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

@login_required
def tambah_stocks(request, book_id):
    book = UploadBook.objects.get(id=book_id)
    book.stocks += 1
    book.save()
    return JsonResponse({'success': True, 'stocks': book.stocks})

@login_required
def kurang_stocks(request, book_id):
    book = UploadBook.objects.get(id=book_id)
    if book.stocks > 0:
        book.stocks -= 1
        book.save()
    if book.stocks == 0:
        book.delete()
        return JsonResponse({'success': True, 'stocks': book.stocks})
    return JsonResponse({'success': True, 'stocks': book.stocks})

@csrf_exempt
def delete_book_ajax(request, id):
    if request.method == 'DELETE':
        book = UploadBook.objects.get(pk=id, user=request.user)
        book.delete()
    
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

        new_book = Book(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image=image, price=price, stocks=stocks, user=user)
        new_book.save()
        upload_book = UploadBook(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image=image, price=price, stocks=stocks, user=user)
        upload_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_books(request):
    product_item = UploadBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

def edit(request, book_id):
    book = get_object_or_404(UploadBook, pk = book_id)
    if request.method == "POST":
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return HttpResponse(b"UPDATED", status=200)
    else:
        form = BookForm(instance=book)