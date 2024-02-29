from django.shortcuts import render
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
django.setup()
from news_app.models import News, ExchangeRates
from django.http import HttpResponse
import logging
from news_app.forms import CurrencyConverterForm


logger = logging.getLogger(__name__)


def news_info(request):
    try:

        publisher_filter = request.GET.get('publisher', 'All')

        if publisher_filter == 'Foreign':
            news_list = News.objects.filter(source_name_country='foreign')
        elif publisher_filter == 'Ukrainian':
            news_list = News.objects.filter(source_name_country='ukrainian')
        else:
            news_list = News.objects.filter()

        context = {'list': news_list, 'publish_filter': publisher_filter}

        return render(request, 'news_app/index.html', context=context)

    except Exception as e:
        logger.error(f"Error occurred {e}")
        return HttpResponse("An error occurred.")


def news_about(request):
    return render(request, 'news_app/about.html')


def exchange_rates(request):

    crypto = ['Bitcoin', 'Ethereum', 'Tether USDt', 'BNB', 'Solana', 'XRP', 'USDC', 'Cardano', 'Avalanche', 'Dogecoin']
    fiat_currencies = ['CNY', 'USD', 'EUR', 'JPY', 'GBP', 'KRW', 'INR', 'CAD', 'HKD', 'UAH']
    all_currency = crypto + fiat_currencies

    currency_filter = request.GET.get('currency', 'All')

    if currency_filter == 'Crypto':
        new_list = ExchangeRates.objects.filter(title__in=crypto)
    elif currency_filter == 'Fiat Currencies':
        new_list = ExchangeRates.objects.filter(title__in=fiat_currencies)
    else:
        new_list = ExchangeRates.objects.filter(title__in=all_currency)

    converted_amount = 0
    form = CurrencyConverterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']

            name = ExchangeRates.objects.filter(title=from_currency)

            conversion_rate = name.first().value
            converted_amount = amount * conversion_rate

    context = {'rate_list': new_list, 'currency_filter': currency_filter, 'convert': converted_amount, 'form': form}
    return render(request, 'news_app/exchange.html', context=context)


def privacy_policy_view(request):
    return render(request, 'news_app/privacy-policy.html')


def terms_conditions_view(request):
    return render(request, 'news_app/terms-conditions.html')


def contact_view(request):
    return render(request, 'news_app/contact.html')
