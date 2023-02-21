import requests
import django


def get_data():
    hey = []
    result = requests.get(
        'https://www.googleapis.com/books/v1/volumes?q=subject:&startIndex=0&maxResults=40&key=AIzaSyBig4wbXKdDJx6TSzrfimU81obiP_rnPFI')

    truc = result.json()["items"]
    for book in truc:
        print(book["volumeInfo"]["authors"])

        hey.append(Book(title=book["volumeInfo"]["title"], authors=book["volumeInfo"]["authors"],
                        publishedDate=book["volumeInfo"]["publishedDate"], description=book["volumeInfo"]["description"])
                   )
    Book.objects.bulk_create(hey)


if __name__ == '__main__':
    django.setup()
    # import AFTER setup
    from app.models import Book

    get_data()


# , authors=book["volumeInfo"]["authors"],
#                         publisher=book["volumeInfo"]["publisher"],
#                         publishedDate=book["volumeInfo"]["publishedDate"],
#                         description=book["volumeInfo"]["description"]