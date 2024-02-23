import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
django.setup()
from news_app.models import News

with open("news.json", "r") as f:
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