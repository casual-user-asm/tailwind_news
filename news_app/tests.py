from django.test import TestCase
from .models import News, ExchangeRates
from django.urls import reverse


class NewsModelTest(TestCase):
    def test_create(self):
        news = News.objects.create(title="M1", url="https://example.com", source_name="Test", source_name_country="ukrainian")
        self.assertEqual(news.title, "M1")
        self.assertEqual(news.url, "https://example.com")
        self.assertEqual(news.source_name, "Test")
        self.assertEqual(news.source_name_country, "ukrainian")


class ExchangeModelTest(TestCase):
    def test_create(self):
        exchange_rates = ExchangeRates.objects.create(title='ZOO', value=52347.0996)
        self.assertEqual(exchange_rates.title, 'ZOO')
        self.assertEqual(exchange_rates.value, 52347.0996)


class ViewsTest(TestCase):
    def setUp(self):
        News.objects.create(title="Test1", url="http://example.com", source_name_country="ukrainian")
        News.objects.create(title="Test2", url="http://example2.com", source_name_country="foreign")
        ExchangeRates.objects.create(title='Test3', value=52347.0996)

    def test_news_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Test1")
        self.assertContains(response, "Test2")

    def test_filter_ukrainian(self):
        response = self.client.get(reverse('index') + '?publisher=Ukrainian')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Test1")
        self.assertNotContains(response, "Test2")

    def test_filter_foreign(self):
        response = self.client.get(reverse('index') + '?publisher=Foreign')
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, "Test1")
        self.assertContains(response, "Test2")

    def test_filter_cryptocurrency(self):
        response = self.client.get(reverse('exchange') + '?currency=Crypto')
        self.assertEqual(response.status_code, 200)

    def test_filter_fiatcurrency(self):
        response = self.client.get(reverse('exchange') + '?currency=Fiat+Currencies')
        self.assertEqual(response.status_code, 200)
