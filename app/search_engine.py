import requests
from bs4 import BeautifulSoup
from typing import List
from b_tree import BTree
from django.db import transaction
from .models import Book, Token, Index

class SearchEngine:
    @staticmethod
    def get_page_text(url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text()

    @staticmethod
    def build_search_index():
        book_urls = Book.objects.values_list('url', flat=True)
        for url in book_urls:
            page_text = SearchEngine.get_page_text(url)
            tokens = page_text.split()
            token_counts = {}
            for token in tokens:
                token = token.lower()
                if len(token) < 2:
                    continue
                if token not in token_counts:
                    token_counts[token] = 1
                else:
                    token_counts[token] += 1

            with transaction.atomic():
                for token, count in token_counts.items():
                    token_obj, _ = Token.objects.get_or_create(word=token)
                    index_obj, _ = Index.objects.get_or_create(book=book, token=token_obj)
                    index_obj.count += count
                    index_obj.save()

    @staticmethod
    def search(query: str) -> List[str]:
        results = []
        query = query.lower()
        tokens = query.split()
        token_objs = Token.objects.filter(word__in=tokens)
        book_counts = {}
        for token_obj in token_objs:
            index_objs = Index.objects.filter(token=token_obj)
            for index_obj in index_objs:
                book_title = index_obj.book.title
                book_count = index_obj.count
                if book_title not in book_counts:
                    book_counts[book_title] = book_count
                else:
                    book_counts[book_title] += book_count

        sorted_books = sorted(book_counts.items(), key=lambda x: x[1], reverse=True)
        for book_title, count in sorted_books:
            results.append(f"{book_title} ({count} occurrences)")

        return results

