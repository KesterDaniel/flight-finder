import os
import requests
from dotenv import load_dotenv
load_dotenv()
TEQUILA_KEY = os.getenv("TEQUILA_API_KEY")

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = TEQUILA_KEY

    def get_city_data(self, city):
        """Getting the data about city from the tequila api"""
        get_city_params = {
            "api_key": self.api_key,
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 2
        }
        get_city_header = {
            "accept": "application/json",
            "apikey": self.api_key
        }

        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=get_city_params, headers=get_city_header)
        response.raise_for_status()
        data = response.json()
        return data
