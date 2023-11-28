from googletrans import Translator
from langdetect import detect
from textblob import TextBlob

def detectLang(text):
    return TextBlob(text).detect_language()

translator = Translator()

def translate(text):
    try:
        lang = detectLang(text)
        return translator.translate(text, src= lang)
    except:
        return translator.translate(text)