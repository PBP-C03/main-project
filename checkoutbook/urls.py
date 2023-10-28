from django.contrib import admin
from django.urls import include, path
from checkoutbook.views import display_order,pay_order,get_order,get_book,inc_book,dec_book,del_book

app_name = 'checkoutbook'

urlpatterns = [
    path('display-order/', display_order, name='display_order'),
    path('pay-order/', pay_order, name='pay_order'),
    path('get-order/', get_order, name='get_order'),
    path('get-book/<int:id>/', get_book, name='get_book'),
    path('inc-book/<int:id>/', inc_book, name='inc_book'),
    path('dec-book/<int:id>/', dec_book, name='dec_book'),
    path('del-book/<int:id>/', del_book, name='del_book'),
]