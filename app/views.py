from django.http import JsonResponse
from rest_framework.views import APIView

from .indexer import search_books
from .serializers import BookSerializer


class Search(APIView):

    def get(self, request):
        serializer = BookSerializer(data=request.data)
        if request.data is not None:
            result = search_books(request.data)
            serializer = BookSerializer(result, many=True)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)