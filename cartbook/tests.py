from django.test import TestCase, Client
from django.contrib.auth.models import User
from book.models import Book
from cartbook.models import Cart, Book_Cart
from django.urls import reverse

class CartbookTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        self.book = Book.objects.create(title='Test Book', price=100)
        self.cart = Cart.objects.create(user=self.user)
        self.book_cart = Book_Cart.objects.create(book=self.book, carts=self.cart, amount=1)

    def test_view_cart(self):
        response = self.client.get(reverse('cartbook:view_cart'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        response = self.client.get(reverse('cartbook:add_to_cart', args=[self.book.id]))
        self.assertRedirects(response, reverse('cartbook:view_cart'))

    def test_remove_from_cart(self):
        response = self.client.get(reverse('cartbook:remove_from_cart', args=[self.book_cart.id]), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_tambah_amount(self):
        response = self.client.get(reverse('cartbook:tambah_amount', args=[self.book_cart.id]), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_kurang_amount(self):
        response = self.client.get(reverse('cartbook:kurang_amount', args=[self.book_cart.id]), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_add_note(self):
        data = {'notes': 'Test note'}
        response = self.client.post(reverse('cartbook:add_note', args=[self.book_cart.id]), data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
