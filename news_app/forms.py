from django import forms
from news_app.models import ExchangeRates


class CurrencyConverterForm(forms.Form):
    all_currency = ['Bitcoin', 'Ethereum', 'Tether USDt', 'BNB', 'Solana', 'XRP', 'USDC', 'Cardano', 'Avalanche', 'Dogecoin', 'CNY', 'USD', 'EUR', 'JPY', 'GBP', 'KRW', 'INR', 'CAD', 'HKD', 'UAH']

    amount = forms.DecimalField(label='Amount', min_value=0.01, error_messages={'required': ''})
    from_currency = forms.ModelChoiceField(queryset=ExchangeRates.objects.filter(title__in=all_currency), label='Currency', error_messages={'required': ''})
