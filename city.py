# API городов https://geocode.maps.co/
# Необходимо реализовать функцию для поиска города по координатам из списка
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("CITY_TOKEN")
base_url = os.getenv("CITY_BASE_URL")

def find_uk_city(coordinates:list) -> str:
    favorite_uk_city = {"Leeds", "London", "Liverpool", "Manchester", "Oxford", "Edinburgh", "Norwich", "York"}
    found_cities = []
    for latitude, longitude in coordinates:
        params = {
            "api_key": token,
            "lat": latitude,
            "lon" : longitude
        }

        response = requests.get(base_url, params=params, timeout=250).json()["address"]["city"].strip().title()
        if response in favorite_uk_city:
            found_cities.append(response)
    return "\n".join(found_cities)

coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]

print(find_uk_city(coordinates))