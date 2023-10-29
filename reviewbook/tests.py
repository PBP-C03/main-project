from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from book.models import Book
from reviewbook.models import Review
from reviewbook.forms import ReviewForm, EditReviewForm
from django.core import serializers
from .views import (
    show_review,
    get_reviews,
    get_reviews_rating,
    get_user_review,
    edit_review,
    add_review,
    delete_review,
)

class ReviewViewTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a book for testing
        self.book = Book.objects.create(title='Test Book', author='Test Author')
        
        # Create a review for the book
        self.review = Review.objects.create(rating=5, review='Test Review', user=self.user, book=self.book)

    def test_show_review_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('reviewbook:show_review', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_get_reviews_view(self):
        response = self.client.get(reverse('reviewbook:get_reviews', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_get_reviews_rating_view(self):
        response = self.client.get(reverse('reviewbook:get_reviews_rating', args=[self.book.id, 5]))
        self.assertEqual(response.status_code, 200)

    def test_get_user_review_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('reviewbook:get_user_review', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_review_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('reviewbook:edit_review', args=[self.book.id, self.review.id]))
        self.assertEqual(response.status_code, 200)

    def test_add_review_view(self):
        self.client.force_login(self.user)
        data = {
            'rating': 4,
            'review': 'New Test Review',
        }
        response = self.client.post(reverse('reviewbook:add_review', args=[self.book.id]), data)
        self.assertEqual(response.status_code, 201)

    def test_delete_review_view(self):
        self.client.force_login(self.user)
        response = self.client.delete(reverse('reviewbook:delete_review', args=[self.book.id, self.review.id]))
        self.assertEqual(response.status_code, 200)

    def test_show_review_view_not_logged_in(self):
        response = self.client.get(reverse('reviewbook:show_review', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_add_review_view_not_logged_in(self):
        data = {
            'rating': 4,
            'review': 'New Test Review',
        }
        response = self.client.post(reverse('reviewbook:add_review', args=[self.book.id]), data)
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_delete_review_view_not_logged_in(self):
        response = self.client.delete(reverse('reviewbook:delete_review', args=[self.book.id, self.review.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_edit_review_view_not_logged_in(self):
        response = self.client.get(reverse('reviewbook:edit_review', args=[self.book.id, self.review.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_edit_review_view_post(self):
        self.client.force_login(self.user)
        data = {
            'rating': 4,
            'review': 'New Test Review',
        }
        response = self.client.post(reverse('reviewbook:edit_review', args=[self.book.id, self.review.id]), data)
        self.assertEqual(response.status_code, 200)

    def test_get_reviews_no_login(self):
        response = self.client.get(reverse('reviewbook:get_reviews', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_get_reviews_rating_no_login(self):
        response = self.client.get(reverse('reviewbook:get_reviews_rating', args=[self.book.id, 5]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_get_user_review_no_login(self):
        response = self.client.get(reverse('reviewbook:get_user_review', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_add_review_no_login(self):
        data = {
            'rating': 4,
            'review': 'New Test Review',
        }
        response = self.client.post(reverse('reviewbook:add_review', args=[self.book.id]), data)
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_delete_review_no_login(self):
        response = self.client.delete(reverse('reviewbook:delete_review', args=[self.book.id, self.review.id]))
        self.assertEqual(response.status_code, 302) 
