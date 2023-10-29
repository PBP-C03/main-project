from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Nota
from book.models import  Book
from cartbook.models import Book_Cart, Cart

class ViewsTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create some sample data for testing
        self.book = Book.objects.create(title='Test Book', stocks=10)
        self.cart = Cart.objects.create(user=self.user)
        self.nota = Nota.objects.create(user=self.user, total_amount=100, total_harga=50, alamat='Test Address', layanan='Test Service')
        self.book_cart = Book_Cart.objects.create(book=self.book, amount=2, carts=self.cart, nota=self.nota)

    def test_display_order(self):
        response = self.client.get(reverse('checkoutbook:display_order'))
        self.assertEqual(response.status_code, 200)

    def test_pay_order(self):
        data = {'Alamat': 'Test Address', 'Layanan': 'Test Service'}
        response = self.client.post(reverse('checkoutbook:pay_order'), data)
        self.assertEqual(response.status_code, 201)

    def test_get_order(self):
        response = self.client.get(reverse('checkoutbook:get_order'))
        self.assertEqual(response.status_code, 200)

    def test_get_order_f(self):
        response = self.client.get(reverse('checkoutbook:get_order'))
        self.assertFalse(response.status_code, 400)

    def test_get_book(self):
        response = self.client.get(reverse('checkoutbook:get_book', kwargs={'id': self.book.pk}))
        self.assertEqual(response.status_code, 200)

    def test_inc_book(self):
        response = self.client.post(reverse('checkoutbook:inc_book', kwargs={'id': self.book.pk}))
        self.assertEqual(response.status_code, 201)

    def test_dec_book(self):
        response = self.client.post(reverse('checkoutbook:dec_book', kwargs={'id': self.book.pk}))
        self.assertEqual(response.status_code, 201)

    def test_del_book(self):
        response = self.client.post(reverse('checkoutbook:del_book', kwargs={'id': self.book.pk}))
        self.assertEqual(response.status_code, 201)

    def test_get_nota(self):
        response = self.client.get(reverse('checkoutbook:get_nota'))
        self.assertEqual(response.status_code, 200)

    def test_get_history(self):
        response = self.client.get(reverse('checkoutbook:get_history'))
        self.assertEqual(response.status_code, 200)

    def test_del_nota(self):
        response = self.client.post(reverse('checkoutbook:del_nota', kwargs={'id': self.nota.pk}))
        self.assertEqual(response.status_code, 201)

    def test_get_desc(self):
        response = self.client.get(reverse('checkoutbook:get_desc', kwargs={'id': self.nota.pk}))
        self.assertEqual(response.status_code, 200)

    def test_get_history(self):
        response = self.client.get(reverse('checkoutbook:get_history', kwargs={'id': self.nota.pk}))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()

