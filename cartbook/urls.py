from django.urls import path
from cartbook.views import view_cart, add_to_cart, remove_from_cart, tambah_amount, kurang_amount, add_note
app_name = 'cartbook'

urlpatterns = [
    path('view-cart/', view_cart, name='view_cart'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:book_cart_id>/', remove_from_cart, name='remove_from_cart'),
    path('tambah-amount/<int:book_cart_id>/', tambah_amount, name='tambah_amount'),
    path('kurang-amount/<int:book_cart_id>/', kurang_amount, name='kurang_amount'),
    path('add-note/<int:book_cart_id>/', add_note, name='add_note'),
   
]
