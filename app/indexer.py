import re
from typing import List

import requests

from .b_tree import BTree
from .models import Book, SearchResult


def build_search_index():
    books = Book.objects.all()
    for book in books:
        # Recuperer le  contenue du livre  dupuis l'URL
        page = requests.get(book.content)
        bookText = page.text
        book_content = bookText

        # Extraction des balise et caractères scripts
        # Enlever les balises HTML et les caractères spéciaux
        book_content = re.sub(r'<.*?>', '', book_content)
        book_content = re.sub(r'[^\w\s]', '', book_content)


        # Tokenize book content
        tokens = re.findall(r'\b\w+\b', book_content)
        # Build B-Tree index
        index = BTree()
        for i, token in enumerate(tokens):
            index.insert(token, i)
        # Search for each token in the book
        for token in index:
            if len(token) < 3:
                continue  # Skip tokens shorter than 3 characters
            if re.match(r'^\d+$', token):
                continue  # Skip tokens containing only digits
            if re.match(r'^<.+>$', token):
                continue  # Skip HTML tags
            count = len(index.search(token))
            SearchResult.objects.create(book=book, token=token, count=count)


def search_books(keyword: str) -> List[SearchResult]:
    results = SearchResult.objects.filter(token=keyword)
    return results