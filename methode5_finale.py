import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

# Fonction pour extraire le texte de la page web en ignorant les balises HTML
def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text)
    return text

# Fonction pour compter les mots les plus fréquents dans une liste de textes
def count_common_words(texts, n):
    words_list = [re.findall('\w+', text.lower()) for text in texts]
    common_words = set(words_list[0]).intersection(*words_list[1:])
    words_counts = Counter([word for words in words_list for word in words if word in common_words])
    return words_counts.most_common(n)

# URLs des pages web à analyser
urls = ['https://www.example.com', 'https://www.example.org', 'https://www.example.net']

# Récupération du texte de chaque page web et stockage dans une liste
texts = [get_text(url) for url in urls]

# Comptage des mots en commun les plus fréquents (10 dans cet exemple)
n = 10
common_words = count_common_words(texts, n)

# Affichage des résultats
print('Les', n, 'mots en commun les plus fréquents sur les pages web sont:')
for word, count in common_words:
    print(word, ':', count)
