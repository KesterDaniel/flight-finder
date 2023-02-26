import os
import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
from data_manager import DataManager
load_dotenv()
TEQUILA_KEY = os.getenv("TEQUILA_API_KEY")

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, cities_data: DataManager):
        self.cities_data = cities_data
        self.cheap_flights = []
        self.api_key = TEQUILA_KEY
        self.locations_url = "https://api.tequila.kiwi.com/locations/query"
        self.search_url = "https://api.tequila.kiwi.com/v2/search"

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

        response = requests.get(url= self.locations_url, params=get_city_params, headers=get_city_header)
        response.raise_for_status()
        data = response.json()
        return data

    def get_flight_data(self):
        """Getting the flight data for city using the city code from get_city_data"""
        cities = self.cities_data.get_cities()
        today = date.today()
        min_return_date = today + relativedelta(days=+7)
        max_return_date = today + relativedelta(days=+28)
        six_months_from_today = today + relativedelta(months=+6)
        for city in cities:
            flight_headers = {
                "accept": "application/json",
                "apikey": self.api_key,
            }

            flight_params = {
                "fly_from": "LON",
                "fly_to": city["iataCode"],
                "date_from": today.strftime("%d/%m/%Y"),
                "date_to": six_months_from_today.strftime("%d/%m/%Y"),
                "curr": "GBP",
                "flight_type": "round",
                "return_from": min_return_date.strftime("%d/%m/%Y"),
                "return_to": max_return_date.strftime("%d/%m/%Y"),
                "limit": 2
            }

            # Getting flight data for city
            flight_data_response = requests.get(url=self.search_url, params=flight_params, headers=flight_headers)
            flight_data_response.raise_for_status()
            data_for_flight = flight_data_response.json()

            # Checking if flight price is lower than the lowest specified in google sheets
            flight_price = int(data_for_flight["data"][0]["price"])
            if flight_price < city["lowestPrice"]:
                flight_details = {
                    "price": flight_price,
                    "departure_city": data_for_flight["data"][0]["cityFrom"],
                    "departure_airport_code": data_for_flight["data"][0]["flyFrom"],
                    "arrival_city": data_for_flight["data"][0]["cityTo"],
                    "arrival_airport_code": data_for_flight["data"][0]["flyTo"],
                    "outbound_date": data_for_flight["data"][0]["route"][0]["local_departure"].split("T")[0],
                    "inbound_date": data_for_flight["data"][0]["route"][0]["local_arrival"].split("T")[0]
                }

                # Adding cheap flights to list
                self.cheap_flights.append(flight_details)

