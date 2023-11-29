from django.shortcuts import render
from book.models import Book
from cartbook.models import Cart, Book_Cart
from checkoutbook.models import Nota
from qna.models import Question, Comment
from reviewbook.models import Review
from main.models import Profile
from uploadbook.models import UploadBook
from cartbook.models import Cart
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core import serializers

@csrf_exempt
def show_main(request):
    books = Book.objects.all()
    context = {
        'user' : request.user,
        'books': books,
    }

    return render(request, "main.html", context)

@csrf_exempt
def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def show_bookcart_json(request):
    book_cart = Book_Cart.objects.all()
    return HttpResponse(serializers.serialize("json", book_cart), content_type="application/json")

@csrf_exempt
def show_cart_json(request):
    cart = Cart.objects.all()
    return HttpResponse(serializers.serialize("json", cart), content_type="application/json")

@csrf_exempt
def show_nota_json(request):
    nota = Nota.objects.all()
    return HttpResponse(serializers.serialize("json", nota), content_type="application/json")

@csrf_exempt
def show_question_json(request):
    question = Question.objects.all()
    return HttpResponse(serializers.serialize("json", question ), content_type="application/json")

@csrf_exempt
def show_comment_json(request):
    comment = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", comment), content_type="application/json")

@csrf_exempt
def show_review_json(request):
    review = Review.objects.all()
    return HttpResponse(serializers.serialize("json", review), content_type="application/json")

@csrf_exempt
def show_uploadbook_json(request):
    uploadbook = UploadBook.objects.all()
    return HttpResponse(serializers.serialize("json", uploadbook), content_type="application/json")

@csrf_exempt
def show_catalog(request):
    books = Book.objects.all()
    context = {
        'user' : request.user,
        'books': books,
        'is_catalog_active': True,
    }

    return render(request, "catalog.html", context)

@csrf_exempt
def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user = user, saldo = 0)
            cart_user = Cart(user = user,total_amount = 0, total_harga = 0)
            profile.save()
            cart_user.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'signup.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('main:login')

@csrf_exempt
@login_required
def account_user(request):
    profile = Profile.objects.get(user = request.user)
    books = UploadBook.objects.all()

    context = {
        'profile' : profile,
        'books' : books
    }
    return render(request,'profile.html',context)

@csrf_exempt
def insert_balance(request):
    if request.method == 'POST':
        jumlah = int(request.POST.get("jumlah"))
        profile = Profile.objects.get(user=request.user)
        profile.saldo += jumlah
        profile.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def get_saldo(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user=request.user)
        print(serialize('json', profile))
        return HttpResponse(serialize('json', profile))
    return HttpResponseNotFound()

@login_required
@csrf_exempt
def tambah_stocks(request, book_id):
    book = UploadBook.objects.get(pk=book_id, user=request.user)
    book.stocks += 1
    book.save()
    return JsonResponse({'success': True, 'stocks': book.stocks})

@login_required
@csrf_exempt
def kurang_stocks(request, book_id):
    book = UploadBook.objects.get(pk=book_id, user=request.user)
    if book.stocks > 0:
        book.stocks -= 1
        book.save()
    if book.stocks == 0:
        book.delete()
        return JsonResponse({'success': True, 'stocks': book.stocks})
    return JsonResponse({'success': True, 'stocks': book.stocks})

@login_required
@csrf_exempt
def delete_book(request, book_id):
    try:
        book = UploadBook.objects.get(id=book_id)
        book.delete()

        return JsonResponse({'success': True})
    except UploadBook.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)




