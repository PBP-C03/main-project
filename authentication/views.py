import json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from cartbook.models import Cart

from main.models import Profile

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
# tes    

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Validasi input
            if not username or not password:
                return JsonResponse({'status': False, 'message': 'Username dan password harus diisi.'}, status=400)

            # Cek apakah username sudah terpakai
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': False, 'message': 'Username sudah digunakan.'}, status=400)

            # Buat user baru
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Buat profil dan keranjang untuk user
            profile = Profile(user=user, saldo=0)
            cart_user = Cart(user=user, total_amount=0, total_harga=0)
            profile.save()
            cart_user.save()

            return JsonResponse({'status': True, 'message': 'Registrasi berhasil.'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'status': False, 'message': 'Request tidak valid.'}, status=400)
    else:
        return JsonResponse({'status': False, 'message': 'Metode request tidak diperbolehkan.'}, status=405)
