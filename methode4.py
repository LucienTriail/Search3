import requests
from bs4 import BeautifulSoup
import re
from collections import Counter


# Code Python qui utilise la méthode d'indexation pour rechercher les mots
# les plus fréquemment répétés dans plusieurs pages web sans compter les balises HTML :

# Fonction pour extraire le texte de la page web en ignorant les balises HTML
def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text)
    return text


# Fonction pour compter les mots les plus fréquents
def count_words(text, n):
    words = re.findall('\w+', text.lower())
    return Counter(words).most_common(n)


# URLs des pages web à analyser
urls = ['https://www.example.com', 'https://www.example.org', 'https://www.example.net']

# Comptage des mots les plus fréquents (10 dans cet exemple) dans chaque page web
n = 10
for url in urls:
    text = get_text(url)
    top_words = count_words(text, n)

    # Affichage des résultats pour chaque page web
    print('Les', n, 'mots les plus fréquents sur la page', url, 'sont:')
    for word, count in top_words:
        print(word, ':', count)
    print('\n')
