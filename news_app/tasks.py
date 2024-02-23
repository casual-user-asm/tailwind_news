

from celery import shared_task
import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
django.setup()
from news_app.models import News
import logging
import subprocess

logger = logging.getLogger(__name__)
file_path = "news.json"

@shared_task
def run_scrapy_spider():
    try:

        try:
            # os.system('rm news.json')
            os.remove(file_path)
        except FileNotFoundError:
            pass

        scrapy_path = "C:\\Users\Влад\Desktop\some\python_projects\\tailwind_news\\venv\Scripts\scrapy.exe"
        spider_path = os.path.join("C:\\Users\Влад\Desktop\some\python_projects\\tailwind_news\\news_app", "news_spider.py")

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
        # raise