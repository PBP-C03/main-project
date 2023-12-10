from django.urls import path
from main.views import show_json, show_main, show_bookcart_json, show_cart_json, show_comment_json, show_nota_json, show_question_json, show_review_json, show_uploadbook_json
from main.views import signup
from main.views import login_user, tambah_stocks, kurang_stocks, delete_book
from main.views import logout_user,show_catalog,account_user,insert_balance,get_saldo,topup

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('catalog/', show_catalog, name='show_catalog'),
    path('json/', show_json, name='show_json'),
    path('cart-json/', show_cart_json, name='show_cart_json'),
    path('bookcart-json/', show_bookcart_json, name='show_bookcart_json'),
    path('nota-json/', show_nota_json, name='show_nota_json'),
    path('question-json/', show_question_json, name='show_question_json'),
    path('comment-json/', show_comment_json, name='show_comment_json'),
    path('review-json/', show_review_json, name='show_review_json'),
    path('uploadbook-json/', show_uploadbook_json, name='show_uploadbook_json'),
    path('account/', account_user, name='account'),
    path('insert_balance/', insert_balance, name='insert_balance'),
    path('get_saldo/', get_saldo, name='get_saldo'),
    path('tambah-stocks/<int:id>', tambah_stocks, name='tambah_stocks'),
    path('kurang-stocks/<int:id>', kurang_stocks, name='kurang_stocks'),
    path('delete-book/<int:id>', delete_book, name='delete_book'),
    path('topup/', topup, name='topup'),
]