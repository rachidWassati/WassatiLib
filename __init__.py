"""
Librairie Wassati

Cette librairie apporte un certains nombre de fonctions afin de faciliter le développement des produits Aligning et Anticipating

Cette librairie contient les modules suivants:

-`divers`: différentes fonctions pour la gestion de fichiers CSV (création, écriture, ...).

-`FullProcessText`: différentes fonctions pour le processing text, ces fonctions vont permettre essentiellement la préparation du contenu text afin d'analyser les textes avec spacy et créer ainsi nos modèles de machine learning.

-`getArguments`: Ce module contient un parser customisé pour saisir des paramètres lors du lancement des commandes dans le terminal.

-`nlp`: Ce module contient des classes et fonctions pour le text processing, mais moins poussé que le module `FullProcessText`.

-`scraper`: Ce module contient un objet Scraper qui va permettre d'aller scraper n'importe quel contenu dans n'importe quel site (excepté les sites construits en React).

-`translator`: Ce module permet de traduire du contenu dans n'importe quelle langue.

Examples:
    >>> from divers.modules import getCurrentDate
    >>> getCurrentDate(['month', 'year'])
    '20229'
    >>> from getArguments.parser import parser
    >>> args = parser(f="file", o="output")
    >>> # $ python main.py -f data.csv -o data_copy.csv
    >>> from scraper.scraper import Scraper
    >>> scraper = Scraper("https://www.scrapbook.com/")
    >>> scraper.isValid()
    True
"""