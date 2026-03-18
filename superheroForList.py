# API по супергероям находится здесь: https://akabab.github.io/superhero-api/api/
# Необходимо реализовать функцию поиска самого умного супергероя среди списка Id, приходящего на вход функции
import os
import requests
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("SUPERHERO_FOR_LIST_URL")
def get_the_smartest_superhero(superheros):
    the_smartest_superhero = ""
    intelligence = 0
    for superhero in superheros:
        url = f"{base_url}/id/{superhero}.json"
        hero = requests.get(url).json()
        if hero["powerstats"]["intelligence"] >= intelligence:
            the_smartest_superhero = hero["name"]
            intelligence = hero["powerstats"]["intelligence"]
    return the_smartest_superhero

print(get_the_smartest_superhero([1, 2, 3]))