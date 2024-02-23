from django.shortcuts import render
from news_app.models import News
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def news_info(request):
    try:

        publisher_filter = request.GET.get('publisher', 'all')

        if publisher_filter == 'foreign':
            news_list = News.objects.filter(source_name_country='foreign')
        elif publisher_filter == 'ukrainian':
            news_list = News.objects.filter(source_name_country='ukrainian')
        else:
            news_list = News.objects.filter()

        context = {'list': news_list, 'publish_filter': publisher_filter}

        return render(request, 'news_app/index.html', context=context)

    except Exception as e:
        logger.error(f"Error occurred {e}")
        return HttpResponse("An error occurred.")