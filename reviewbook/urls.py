from django.urls import path
from reviewbook.views import show_review, add_review, delete_review, get_reviews, get_reviews_rating, get_user_review, edit_review, create_review_flutter

app_name = 'reviewbook'

urlpatterns = [
    path('<int:id>/', show_review, name="show_review"),
    path('<int:id>/add-review/', add_review, name="add_review"),
    path('<int:id>/delete-review/<int:reviewId>/', delete_review, name="delete_review"),
    path('<int:id>/get-reviews/', get_reviews, name="get_reviews"),
    path('<int:id>/get-reviews/<int:rating>/', get_reviews_rating, name="get_reviews_rating"),
    path('<int:id>/get-user-review/', get_user_review, name="get_user_review"),
    path('<int:id>/edit-review/<int:reviewId>/', edit_review, name="edit_review"),
    path('<int:id>/create_review_flutter/', create_review_flutter, name="create_review_flutter"),
]