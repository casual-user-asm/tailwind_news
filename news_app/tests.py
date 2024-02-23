from django.test import TestCase
from .models import News
from django.urls import reverse


class NewsModelTest(TestCase):
    def test_create(self):
        news = News.objects.create(title="M1", url="https://example.com", source_name="Test", source_name_country="ukrainian")
        self.assertEqual(news.title, "M1")
        self.assertEqual(news.url, "https://example.com")
        self.assertEqual(news.source_name, "Test")
        self.assertEqual(news.source_name_country, "ukrainian")


class ViewsTest(TestCase):
    def setUp(self):
        News.objects.create(title="Test1", url="http://example.com", source_name_country="ukrainian")
        News.objects.create(title="Test2", url="http://example2.com", source_name_country="foreign")

    def test_news_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response,"Test1")
        self.assertContains(response,"Test2")

    def test_filter_ukrainian(self):
        response = self.client.get(reverse('index') + '?publisher=ukrainian')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response,"Test1")
        self.assertNotContains(response,"Test2")

    def test_filter_foreign(self):
        response = self.client.get(reverse('index') + '?publisher=foreign')
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response,"Test1")
        self.assertContains(response,"Test2")