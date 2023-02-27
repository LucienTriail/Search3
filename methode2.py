import requests


def construire_index(texte):
    """
    Cette fonction construit un index qui répertorie les positions de chaque mot dans une chaîne de caractères.

    Args:
        texte (str): La chaîne de caractères à indexer.

    Returns:
        dict: Un dictionnaire qui associe à chaque mot la liste de ses positions dans la chaîne de caractères.
    """
    mots = texte.split()
    index = {}
    for i, mot in enumerate(mots):
        if mot not in index:
            index[mot] = []
        index[mot].append(i)
    return index


def rechercher_occurrences(texte, mot):
    """
    Cette fonction recherche toutes les occurrences d'un mot dans une chaîne de caractères en utilisant un index.

    Args:
        texte (str): La chaîne de caractères dans laquelle on recherche le mot.
        mot (str): Le mot à rechercher.

    Returns:
        list: Une liste qui contient les positions de toutes les occurrences du mot dans la chaîne de caractères.
    """
    index = construire_index(texte)
    if mot in index:
        return index[mot]
    else:
        return []


# Recherche toutes les occurrences d'un mot dans une chaîne de caractères en dur
texte = "La programmation est amusante, mais difficile."
mot = "programmation"
occurrences = rechercher_occurrences(texte, mot)
nb_occurrences = len(occurrences)
print(f"Le mot '{mot}' apparaît {nb_occurrences} fois dans le texte aux positions suivantes : {occurrences}.")

# Recherche toutes les occurrences d'un mot dans une page web
url = "https://www.example.com"
page = requests.get(url)
texte = page.text
mot = "example"
occurrences = rechercher_occurrences(texte, mot)
nb_occurrences = len(occurrences)
print(f"Le mot '{mot}' apparaît {nb_occurrences} fois dans la page web aux positions suivantes : {occurrences}.")
