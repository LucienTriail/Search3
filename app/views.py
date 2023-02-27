from django.http import JsonResponse
from rest_framework.views import APIView

from .indexer import search_books
from .methods import search_all_fields
from .serializers import BookSerializer


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
        serializer = BookSerializer(data=self.request.query_params.get('q'))
        print('lkfkfk', self.request.query_params.get('q'))
        if self.request.query_params.get('q') is not None:
            print('ici')
            result = search_books(self.request.query_params.get('q'))
            print('result', result)
            serializer = BookSerializer(result, many=True)
            print('serializer', serializer.data)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, status=400)


class Seyba(APIView):
    def get(self, request):
        return JsonResponse()