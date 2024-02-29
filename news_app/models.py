from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    source_name = models.CharField(max_length=255)
    source_name_country = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ExchangeRates(models.Model):
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.title
