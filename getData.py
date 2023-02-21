import requests
import django


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
    from app.methods import search_all_fields
    from app.models import Book
    for i in range(31,100):

        get_data(i)


    # Book.objects.all().delete()
    #search_all_fields("earth")
