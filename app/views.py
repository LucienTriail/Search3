from django.core import serializers
from django.http import JsonResponse
from rest_framework.views import APIView

from .indexer import search_books_per
from .methods import search_all_fields
from .models import Book
from .serializers import BookSerializer, SearchResultSerializer


class Search(APIView):

    def get(self, request):
        serializer = BookSerializer(data=self.request.query_params.get('q'))
        print('lkfkfk', self.request.query_params.get('q'))
        if self.request.query_params.get('q') is not None:
            print('ici')
            result = search_all_fields(self.request.query_params.get('q'))
            print('result', result)
            serializer = BookSerializer(result, many=True)
            print('serializer', serializer.data)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, status=400)


class Issouf(APIView):
    def get(self, request):
        serializer = SearchResultSerializer(data=self.request.query_params.get('q'))
        # print('lkfkfk', self.request.query_params.get('q'))
        if self.request.query_params.get('q') is not None:
            print('ici')
            result = search_books_per(self.request.query_params.get('q'))
            # print('result', result)
            # truc ={
            #     "title":result.book.title,
            #     "author": result.book.authors[0],
            #     "count": result.count
            #
            # }

            serializer = SearchResultSerializer(result, many=True)
            print('serializer', serializer.data)
            return JsonResponse(serializer.data, safe=False)



class Seyba(APIView):
    def get(self, request):
        qs = Book.objects.all()
        serializer = serializers.serialize('json', qs)
        print("djdj", serializer)
        print('dddddddd')
        return JsonResponse(serializer, safe=False)