import django
import requests

# from app.models import Book



def get_data(number):
    hey = []
    val = str(number)
    result2 = requests.get(f"https://gutendex.com/books/?page={val}")
    truc2 = result2.json()["results"]
    for book in truc2:

        try:

            #print(book["formats"]["text/html"], "$$$$$$$$$$$$$$ ")

            hey.append(Book(title=book["title"], authors=book["authors"],
                            category=book["subjects"],
                            content=book["formats"]["text/html"]))
        except KeyError:
            continue

    Book.objects.bulk_create(hey)


if __name__ == '__main__':
    django.setup()
    # import AFTER setup
    # from app.methods import search_all_fields
    '''
    from app.models import Book
    for i in range(1, 10):
        get_data(i)
    '''


    # Book.objects.all().delete()
    from app.models import Book
    from app.indexer import search_books, build_search_index, search_books_by, search_books_Per

    print("41 getData")
    # build_search_index()
    # Recherche des livres contenant le mot clé "Python"
    #results = search_books("Romeo")
    # results = search_books_by("Romeo")
    results = search_books_Per("Romeo")

    # Affichage des résultats
    for result in results:
        print(result)
        # book_id = result['book']
        # book = Book.objects.get(id=book_id)
        # book_title = book.title
        #
        # print(type(result))
        # print(book, ',', result['count'] )
        #print(result)
        # print(result, result.count)
        # print(f"Token: {result.token}, Book: {result.book.title}, Count: {result.count}")
        #print(f"Token: {result['token']}, Book: {result['book__title']}, Count: {result['count']}")

    # print(res)
    # for data in res:
    #     print('Test')
    #     print(data)