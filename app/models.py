from django.db import models
from django.contrib.postgres.indexes import GinIndex


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pub_date = models.DateField()
    category = models.TextField()
    ebook_no = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    credits = models.TextField()
    description = models.TextField()
    downloads = models.IntegerField()
    content = models.TextField()


    class Meta:
        indexes = [
            GinIndex(fields=['pub_date', 'title', 'author', 'content',  'description', 'downloads', 'category', 'ebook_no', 'price' ] , name='books_index')
        ]



