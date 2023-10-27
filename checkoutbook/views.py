from django.shortcuts import render
from django.shortcuts import render
from book.models import Book
from main.models import Profile
from checkoutbook.models import Nota
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
# Create your views here.



def checkout_cart(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        payment = 0
        if profile.saldo >= payment :
            profile.saldo -= payment
            profile.save()
            nota = Nota(user = profile.user, amount = payment)
            nota.save()
            return HttpResponse(b"PAYMENT SUCCEED", status=201)
        else:
            return HttpResponse(b"PAYMENT FAILED", status=403)

    return HttpResponseNotFound()

def get_nota_ajax(request):
    if request.method == 'POST':
        nota = Nota.objects.filter(user = request.user)

        return HttpResponse(b"SUCCEED", status=201)

    return HttpResponseNotFound()
