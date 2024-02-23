from django.urls import path
from .views import news_info


urlpatterns = [
    path('', news_info, name='index'),
]
