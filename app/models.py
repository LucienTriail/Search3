import ast

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from django.db import models


# isbn_10 = models.TextField()
#     isbn_13 = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=8000)
    authors = ArrayField(models.CharField(max_length=8000))
    content = models.URLField(max_length=500)
    category = ArrayField(models.CharField(max_length=8000))

    class Meta:
        indexes = [
            GinIndex(fields=['title', 'authors', 'category'], name='books_index')
        ]

    def __str__(self):
        author_dict = ast.literal_eval(self.authors[0])
        author_name = author_dict.get("name")
        author_name = author_name.replace(',', '-')
        return f"{self.title}, {author_name}"


# class wordTree(models.Model):
#     token  = models.CharField(max_length=8000)
#     result = ArrayField(models.CharField(max_length=8000))

class SearchResult(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.token} ({self.count}) in {self.book.title}"


class SearchResultObject:
    def __init__(self, book, count):
        self.book = book
        self.count = count

    def __str__(self):
        return f"{self.book}, {self.count} "