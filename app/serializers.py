from rest_framework import serializers

from .models import Book, SearchResultObject


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class SearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchResultObject
        fields = '__all__'