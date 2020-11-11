import requests
from bs4 import BeautifulSoup as bs
import re

class Scraper:
    # Regex qui permet de verifier la validite d'une URL
    regex = re.compile(
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»""'']))"
        )

    def __init__(self, url):
        self.url = url

    def isValid(self):
        return re.match(self.regex, self.url) is not None

    @classmethod
    def scrapContent(self, url):
        req = requests.get(url)
        content = req.content
        soup = bs(content, "html.parser")
        balises = set([text.parent.name for text in soup.find_all(text= True)])
        textContent = []

        if 'h1' in balises:
            allH1 = soup.findAll('h1')
            for h1 in allH1:
                textContent.append(h1)
        if 'h2' in balises:
            allH2 = soup.findAll('h2')
            for h2 in allH2:
                textContent.append(h2)
        if 'h3' in balises:
            allH3 = soup.findAll('h3')
            for h3 in allH3:
                textContent.append(h3)
        if 'p' in balises:
            allP = soup.findAll('p')
            for p in allP:
                textContent.append(p)
        if 'ul' in balises:
            allUl = soup.findAll('ul')
            for ul in allUl:
                textContent.append(ul)

        elements = [element.text for element in textContent if not isinstance(element, type('str'))]
        # Remove duplicates
        allTexts = []
        allTexts = [element for element in elements if element not in allTexts]
        allTexts = [' '.join(text.split()) for text in allTexts]

        return ' '.join(allTexts)

    def launchScrap(self):
        if self.isValid():
            if not self.url.startswith("http"):
                newUrl = "http://" + self.url
                text = self.scrapContent(newUrl)
            else:
                text = self.scrapContent(self.url)

        return text