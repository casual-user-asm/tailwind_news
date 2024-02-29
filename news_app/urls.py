from django.urls import path
from .views import news_info, news_about, exchange_rates, privacy_policy_view, terms_conditions_view, contact_view


urlpatterns = [
    path('', news_info, name='index'),
    path('about/', news_about, name='about'),
    path('exchange/', exchange_rates, name='exchange'),
    path('privacy_policy/', privacy_policy_view, name='privacy_policy'),
    path('terms_conditions/', terms_conditions_view, name='terms_conditions'),
    path('contact/', contact_view, name='contact'),
]
