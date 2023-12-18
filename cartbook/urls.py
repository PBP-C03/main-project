from django.urls import path
from cartbook.views import *

app_name = 'cartbook'

urlpatterns = [
    path('view-cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:book_cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('tambah-amount/<int:book_cart_id>/', tambah_amount, name='tambah_amount'),
    path('kurang-amount/<int:book_cart_id>/', kurang_amount, name='kurang_amount'),
    path('add-note/<int:book_cart_id>/', add_note, name='add_note'),
    path('remove-from-cart-json/', remove_from_cart_json, name='remove_from_cart_json'),
    path('tambah-amount-json/', tambah_amount_json, name='tambah_amount_json'),
    path('kurang-amount-json/', kurang_amount_json, name='kurang_amount_json'),
    path('add-note-json/', add_note_json, name='add_note_json'),
   
]
