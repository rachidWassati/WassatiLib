from googletrans import Translator
from langdetect import detect

def detectLang(text):
    return detect(text)

translator = Translator()

def translate(text):
    try:
        lang = detectLang(text)
        return translator.translate(text, src= lang)
    except:
        return translator.translate(text)