from celery import shared_task
import os
import json
import django
from news.settings import BASE_DIR
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
django.setup()
from news_app.models import News, ExchangeRates
import logging
import subprocess
import requests
import environ

env = environ.Env(
    openexchangerates_key=(str),
    coinmarketcap_key=(str),
)
environ.Env.read_env(BASE_DIR / '.env')

logger = logging.getLogger(__name__)
file_path = "news.json"


@shared_task
def run_scrapy_spider():
    try:

        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass

        scrapy_path = "/home/casual/news_server/venv/bin/scrapy"
        spider_path = os.path.join("/home/casual/news_server/tailwindnews/news_app", "news_spider.py")

        command = [scrapy_path, 'runspider', spider_path, '-o', "news.json"]

        subprocess.run(command)

        News.objects.all().delete()

        with open(file_path, "r") as f:
            data1 = json.load(f)
            for i in data1:
                i["title"] = i["title"].replace('\xa0', ' ')
                i["url"] = i["url"].replace('\xa0', ' ')
            for k in data1:
                title = k['title']
                url = k['url']
                source = k['source']
                source_country = k['source_country']
                News.objects.create(title=title, url=url, source_name=source, source_name_country=source_country)
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


@shared_task
def take_rates():
    # Take currency rate
    url = f"https://openexchangerates.org/api/latest.json?app_id={env('openexchangerates_key')}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    rates = response.text
    data_dict = json.loads(rates)
    # Take cryptocurrency rate
    url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'sort': 'cmc_rank',
        'start': 1,
        'limit': 10,
    }
    headers2 = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': env('coinmarketcap_key'),
    }

    response2 = requests.get(url, headers=headers2)
    data = json.loads(response2.text)

    ExchangeRates.objects.all().delete()

    for i in data['data']:
        ExchangeRates.objects.create(title=i['name'], value=i['quote']['USD']['price'])

    for title, value in data_dict['rates'].items():
        ExchangeRates.objects.create(title=title, value=value)
