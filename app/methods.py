from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import Book


def search_all_fields(q):
    vector = SearchVector('title', 'authors',  'category')
    query = SearchQuery(q, search_type='phrase')
    result = Book.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
    #print(result[0].authors)
    # treeByWord(result, q)
    return result


def getAllBooks():
    return  Book.objects.all()

# def treeByWord(result, wordkey):
#     for book in result:
#         print('Test')
#         print(book)

    # booksRes = result.json()["results"]


# search_all_fields("earth")