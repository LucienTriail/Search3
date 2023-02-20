from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

from .serializers import BookSerializer
from .methods import *


class Search(APIView):

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if request.data is not None:
            result = search_all_fields(request.data)
            serializer = BookSerializer(result,many=True)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
