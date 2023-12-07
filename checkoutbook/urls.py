from django.contrib import admin
from django.urls import include, path
from checkoutbook.views import display_order,pay_order,get_order,get_book,inc_book,dec_book,del_book,get_nota,del_nota,get_desc,get_history,get_cart
from checkoutbook.views import get_all_order,get_user,set_book_mob

app_name = 'checkoutbook'

urlpatterns = [
    path('display-order/', display_order, name='display_order'),
    path('pay-order/', pay_order, name='pay_order'),
    path('get-cart/', get_cart, name='get_cart'),
    path('get-order/', get_order, name='get_order'),
    path('get-book/<int:id>/', get_book, name='get_book'),
    path('inc-book/<int:id>/', inc_book, name='inc_book'),
    path('dec-book/<int:id>/', dec_book, name='dec_book'),
    path('del-book/<int:id>/', del_book, name='del_book'),
    path('get-nota/', get_nota, name='get_nota'),
    path('del-nota/<int:id>/', del_nota, name='del_nota'),
    path('get-desc/<int:id>/', get_desc, name='get_desc'),
    path('get-history/<int:id>/', get_history, name='get_history'),
    path('get-all-order/', get_all_order, name='get_all_order'),
    path('get-user/', get_user, name='get_user'),

    path('set-book-mob/', set_book_mob, name='set_book_mob'),


]