

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Book
def search_all_fields(q):
    vector= SearchVector('title','author','content','description')
    query = SearchQuery(q,search_type='phrase')
    list  =Book.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
    return list
