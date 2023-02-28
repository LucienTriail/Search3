import re
from typing import List

import requests
from django.db.models import Count

from .b_tree import BTree
from .methods import search_all_fields
from .models import Book, SearchResult, SearchResultObject


def build_search_index():
    # Récupérer les 10 premiers livres
    books = Book.objects.all()[:5]
    for book in books:
        # Récupérer le contenu du livre depuis l'URL
        page = requests.get(book.content)
        book_text = page.text
        book_content = book_text

        # Extraction des balises et caractères scripts
        # Enlever les balises HTML et les caractères spéciaux
        book_content = re.sub(r'<.*?>', '', book_content)
        book_content = re.sub(r'[^\w\s]', '', book_content)

        # Tokenize book content
        tokens = re.findall(r'\b\w+\b', book_content)

        # Build B-Tree index
        index = BTree(t=2)
        for i, token in enumerate(tokens):
            index.insert(token, i)

        # Search for each token in the book
        for token in index.traverse():
            if len(token) < 3:
                continue  # Skip tokens shorter than 3 characters
            if re.match(r'^\d+$', token):
                continue  # Skip tokens containing only digits
            if re.match(r'^<.+>$', token):
                continue  # Skip HTML tags

            results = index.search(token)
            count = len(results) if results is not None else 0
            # tf = count / float(len(tokens))
            SearchResult.objects.create(book=book, token=token, count=count)


def search_books(keyword: str) -> List[SearchResult]:
    results = SearchResult.objects.filter(token=keyword)
    return list(results)


def search_books_by(keyword: str) -> List[SearchResult]:
    results = (
        SearchResult.objects
        .filter(token=keyword)
        .values('token', 'book')
        .annotate(count=Count('id'))
    )
    search_results = []
    for result in results:
        book_id = result['book']
        book = Book.objects.get(id=book_id)
        book_title = book.title
        search_result_object = SearchResultObject(book=book, count=result['count'])
        search_results.append(search_result_object)

    return search_results


def search_books_per(keyword: str) -> List[SearchResultObject]:
    book_list = search_all_fields(keyword)
    results = (
        SearchResult.objects
        .filter(token=keyword)
        .values('token', 'book')
        .annotate(count=Count('id'))
    )
    search_results = []
    for result in results:
        book_id = result['book']
        book = Book.objects.get(id=book_id)
        title = book.title
        author = book.authors[0]
        search_result_object = SearchResultObject(book=book, count=result['count'], title=title, author=author)
        search_results.append(search_result_object)

    sorted_results = []
    for book in book_list:
        for search_result in search_results:
            if search_result.book == book:
                sorted_results.append(search_result)

    for search_result in search_results:
        if search_result not in sorted_results:
            sorted_results.append(search_result)

    return sorted_results


'''
GOOD Version but not optimal

from typing import List
import requests
from .b_tree import BTree
from .models import Book, SearchResult
import re


def build_search_index():
    # Récupérer les 10 premiers livres
    books = Book.objects.all()[:5]
    for book in books:
        print(book.title , 'build_search_index')
        # Récupérer le contenu du livre depuis l'URL
        page = requests.get(book.content)
        book_text = page.text
        book_content = book_text

        # Extraction des balises et caractères scripts
        # Enlever les balises HTML et les caractères spéciaux
        book_content = re.sub(r'<.*?>', '', book_content)
        book_content = re.sub(r'[^\w\s]', '', book_content)

        # Tokenize book content
        tokens = re.findall(r'\b\w+\b', book_content)

        # Build B-Tree index
        index = BTree(t=2)
        for i, token in enumerate(tokens):
            index.insert(token, i)

        # Search for each token in the book
        for token in index.traverse():
            if len(token) < 3:
                continue  # Skip tokens shorter than 3 characters
            if re.match(r'^\d+$', token):
                continue  # Skip tokens containing only digits
            if re.match(r'^<.+>$', token):
                continue  # Skip HTML tags

            if index.search(token):
                res = index.search(token)
                count = len(res) if res is not None else 0
                # tf = count / float(len(tokens))
            else:
                continue
            # count = len(index.search(token))
            SearchResult.objects.create(book=book, token=token, count=count)


def search_books(keyword: str) -> List[SearchResult]:
    results = SearchResult.objects.filter(token=keyword)
    return list(results)
'''