# API словаря яндекса находится здесь https://yandex.ru/dev/dictionary/
# Необходимо реализовать функцию для перевода слова с русского языка на английский
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("YANDEX_TOKEN")
base_url = os.getenv("YANDEX_BASE_URL")

def translate_word(word):
    params = {
        "key": token,
        "lang": "ru-en",
        "text" : word
    }

    response = requests.get(base_url, params=params).json()["def"][0]["tr"][0]["text"]
    return response

print(translate_word("машина"))