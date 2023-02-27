import requests


def recherche_mot(texte, mot):
    """
    Cette fonction recherche le nombre d'occurrences d'un mot dans une chaîne de caractères.

    Args:
        texte (str): La chaîne de caractères dans laquelle on recherche le mot.
        mot (str): Le mot à rechercher.

    Returns:
        int: Le nombre d'occurrences du mot dans la chaîne de caractères.
    """
    occurrences = 0
    mots = texte.split()
    for m in mots:
        if m == mot:
            occurrences += 1
    return occurrences


# Recherche le nombre d'occurrences d'un mot dans une chaîne de caractères en dur
texte = "La programmation est amusante, mais difficile."
mot = "programmation"
nb_occurrences = recherche_mot(texte, mot)
print(f"Le mot '{mot}' apparaît {nb_occurrences} fois dans le texte.")

# Recherche le nombre d'occurrences d'un mot dans une page web
url = "https://www.example.com"
page = requests.get(url)
texte = page.text
mot = "example"
nb_occurrences = recherche_mot(texte, mot)
print(f"Le mot '{mot}' apparaît {nb_occurrences} fois dans la page web.")


def findWord(word, bookUrl):
    contentBook = requests.get(bookUrl)
    txtContent = contentBook.text
    nbOcc = recherche_mot(txtContent, word)
    return (word, nbOcc)
