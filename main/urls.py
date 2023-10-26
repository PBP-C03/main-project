from django.urls import path
from main.views import show_main
from main.views import signup
from main.views import login_user
from main.views import logout_user,show_catalog,account_user,insert_balance,get_saldo

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('catalog/', show_catalog, name='show_catalog'),

    path('account/', account_user, name='account'),
    path('insert_balance/', insert_balance, name='insert_balance'),
    path('get_saldo/', get_saldo, name='get_saldo'),
]