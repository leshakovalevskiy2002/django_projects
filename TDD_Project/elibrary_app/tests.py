from http import HTTPStatus
from .views import home
from django.test import TestCase, SimpleTestCase
from django.urls import resolve
from .models import Catalog
from django.shortcuts import reverse


class ElibraryURLsTest(SimpleTestCase):
    """    Тестируем URLs    """

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


class CatalogModelTests(TestCase):
    """    Тест модели каталога    """

    def setUp(self):
        self.book = Catalog(
            title='First Django Book',
            ISBN='978-1-60309-3',
            author='Ilya Perminov',
            price='9.99',
            availability='True'
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalog)

    def test_str_representation(self):
        self.assertEqual(str(self.book), "First Django Book")

    def test_saving_and_retrieving_book(self):
        first_book = Catalog()
        first_book.title = 'First Django Book'
        first_book.ISBN = '978-1-60309-3'
        first_book.author = 'Ilya Perminov'
        first_book.price = '9.99'
        first_book.availability = 'True'
        first_book.save()

        second_book = Catalog()
        second_book.title = 'Second Django Book'
        second_book.ISBN = '978-3-60124-1'
        second_book.author = 'Dmitry Seleznev'
        second_book.price = '19.99'
        second_book.availability = 'False'
        second_book.save()

        saved_books = Catalog.objects.all()
        self.assertEqual(saved_books.count(), 2)

        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'First Django Book')
        self.assertEqual(second_saved_book.author, 'Dmitry Seleznev')