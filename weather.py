import os
import requests
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.environ.get('API_KEY')
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
def query_api(city):
    try:
        url = API_URL.format(city, API_KEY)
        print(f"Requesting: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        if 'cod' in data and data['cod'] != 200:
            print(f"Error: {data.get('message')}")
            return None
    except Exception as exc:
        print(f"An error occurred: {exc}")
        data = None
    return data

