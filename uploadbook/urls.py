from django.urls import path
from uploadbook.views import get_books, add_book_ajax, add_book, delete_book, kurang_stocks, tambah_stocks, edit_book

app_name = 'uploadbook'

urlpatterns = [
    path('get-book/', get_books, name='get_books'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:id>', edit_book, name='edit_book'),
    path('tambah-stocks/<int:id>', tambah_stocks, name='tambah_stocks'),
    path('kurang-stocks/<int:id>', kurang_stocks, name='kurang_stocks'),
    path('delete-book/<int:id>', delete_book, name='delete_book'),
]