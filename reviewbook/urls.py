from django.urls import path
from reviewbook.views import show_main, add_review_ajax, delete_review_ajax, get_reviews_ajax

app_name = 'reviewbook'

urlpatterns = [
    path('<int:id>/', show_main, name="show_main"),
    path('add-reqview/', add_review_ajax, name="add_review_ajax"),
    path('delete-review/<int:id>/', delete_review_ajax, name="delete_review_ajax"),
    path('get-reviews/<int:id>/', get_reviews_ajax, name="get_reviews_ajax")
]