from django.shortcuts import render
from book.models import Book
from main.models import Profile
from uploadbook.models import UploadBook
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

def show_main(request):
    books = Book.objects.all()
    context = {
        'user' : request.user,
        'books': books,
    }

    print(request.user.is_authenticated)
    return render(request, "main.html", context)

def show_catalog(request):
    books = Book.objects.all()
    context = {
        'user' : request.user,
        'books': books,
        'is_catalog_active': True,
    }

    return render(request, "catalog.html", context)

def signup(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user = user, saldo = 0)
            profile.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'signup.html', context)

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

@login_required
def account_user(request):
    profile = Profile.objects.get(user = request.user)
    books = UploadBook.objects.get(user = request.user)

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

    
def get_saldo(request):
    if request.method == 'GET':
        profile = Profile.objects.filter(user=request.user)
        print(serialize('json', profile))
        return HttpResponse(serialize('json', profile))
    return HttpResponseNotFound()