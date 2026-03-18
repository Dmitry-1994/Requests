# API по супергероям находится здесь: https://akabab.github.io/superhero-api/api/
# Необходимо реализовать функцию поиска самого умного супергероя среди Hulk, Captain America, Thanos
import os
import requests
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPERHERO_URL")
heroes = requests.get(url).json()

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ""
    intelligence = 0
    heroes_name_list = ["Hulk", "Captain America", "Thanos"]
    for hero in heroes:
        if hero["name"] in heroes_name_list and hero["powerstats"]["intelligence"] >= intelligence:
            the_smartest_superhero = hero["name"]
            intelligence = hero["powerstats"]["intelligence"]
    return the_smartest_superhero

print(get_the_smartest_superhero())