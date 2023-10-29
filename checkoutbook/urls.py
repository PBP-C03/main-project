from django.contrib import admin
from django.urls import include, path
from checkoutbook.views import display_order,pay_order,get_order,get_book,inc_book,dec_book,del_book,get_nota,del_nota,get_desc

app_name = 'checkoutbook'

urlpatterns = [
    path('display-order/', display_order, name='display_order'),
    path('pay-order/', pay_order, name='pay_order'),
    path('get-order/', get_order, name='get_order'),
    path('get-book/<int:id>/', get_book, name='get_book'),
    path('inc-book/<int:id>/', inc_book, name='inc_book'),
    path('dec-book/<int:id>/', dec_book, name='dec_book'),
    path('del-book/<int:id>/', del_book, name='del_book'),
    path('get-nota/', get_nota, name='get_nota'),
    path('del-nota/<int:id>/', del_nota, name='del_nota'),
    path('get-desc/<int:id>/', get_desc, name='get_desc'),
]