from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    source_name = models.CharField(max_length=255)
    source_name_country = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
