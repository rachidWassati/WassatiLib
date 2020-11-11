from .customStopWords import customStopWordsFR
from stop_words import get_stop_words
import string
import spacy
import re

class TextProcess:

    def __init__(self, lang):
        self.lang = lang
        if self.lang == 'fr':
            self.nlp = spacy.load('fr_core_news_sm') # disable= ['parser','ner']
        if self.lang == 'en':
            self.nlp = spacy.load('en_core_web_lg')

    def cleanText(self, text):
        '''
        Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers and urls
        '''
        text = str(text).lower()
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub(r'\w*\d\w*', '', text)
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

        return text

    def addCustomStopwords(self, lang):
        custom_stopwords = []
        for m in get_stop_words(lang):
            custom_stopwords.append(m)
        for w in customStopWordsFR():
            custom_stopwords.append(w)
        for word in get_stop_words('en'):
            custom_stopwords.append(word)

        return custom_stopwords

    def lemmatizer(self, text):
        
        doc = self.nlp(text)
        result = []
        for token in doc:
            if token.text in self.addCustomStopwords('fr'):
                continue
            if token.is_punct:
                continue
            if token.lemma_ == '-PRON-':
                continue
            if token.lemma_ == '-VERB-':
                continue
            result.append(token.lemma_)

        return " ".join(result)