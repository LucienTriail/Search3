import requests
import re

# Code Python qui utilise la méthode d'indexation pour rechercher les mots les plus fréquemment répétés
# dans une page web. Cette méthode consiste à construire un index qui répertorie les positions de chaque
# mot dans la chaîne de caractères, puis à compter le nombre d'occurrences de chaque mot dans l'index

def construire_index(texte):
    """
    Cette fonction construit un index qui répertorie les positions de chaque mot dans une chaîne de caractères.

    Args:
        texte (str): La chaîne de caractères à indexer.

    Returns:
        dict: Un dictionnaire qui associe à chaque mot la liste de ses positions dans la chaîne de caractères.
    """
    mots = re.findall(r'\w+', texte.lower())
    index = {}
    for i, mot in enumerate(mots):
        if mot not in index:
            index[mot] = []
        index[mot].append(i)
    return index


def compter_occurrences(index):
    """
    Cette fonction compte le nombre d'occurrences de chaque mot dans un index.

    Args:
        index (dict): Un dictionnaire qui associe à chaque mot la liste de ses positions dans une chaîne de caractères.

    Returns:
        dict: Un dictionnaire qui associe à chaque mot le nombre de fois qu'il apparaît dans la chaîne de caractères.
    """
    occurrences = {}
    for mot, positions in index.items():
        occurrences[mot] = len(positions)
    return occurrences


def trouver_mots_plus_repeter(texte, n):
    """
    Cette fonction trouve les n mots les plus fréquemment répétés dans une chaîne de caractères.

    Args:
        texte (str): La chaîne de caractères à analyser.
        n (int): Le nombre de mots à trouver.

    Returns:
        list: Une liste qui contient les n mots les plus fréquemment répétés dans la chaîne de caractères.
    """
    index = construire_index(texte)
    occurrences = compter_occurrences(index)
    mots = sorted(occurrences, key=occurrences.get, reverse=True)
    return mots[:n]


# Trouve les 10 mots les plus fréquemment répétés dans une page web
url = "https://www.example.com"
page = requests.get(url)
texte = page.text
n = 10
mots_plus_repeter = trouver_mots_plus_repeter(texte, n)
print(f"Les {n} mots les plus fréquemment répétés dans la page web sont : {mots_plus_repeter}.")
