import requests

class DataManager:
    def __init__(self):
        self.get_url = "https://api.sheety.co/67381695094c88fc68cb8d316be6f66a/flightDeals/prices"


    def get_cities(self):
        """Getting all data about cities from our google sheet"""
        response = requests.get(url=self.get_url)
        response.raise_for_status()
        cities_data = response.json()
        all_cities = cities_data["prices"]
        return all_cities



