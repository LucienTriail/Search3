from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.postgres.indexes import GinIndex


# isbn_10 = models.TextField()
#     isbn_13 = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = ArrayField(models.CharField(max_length=255))
    category = ArrayField(models.CharField(max_length=2000))
    content = models.CharField(max_length=500)

    class Meta:
        indexes = [
            GinIndex(fields=['title', 'category', 'authors', 'content'], name='books_index')
        ]
