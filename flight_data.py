from data_manager import DataManager
from flight_search import FlightSearch
import requests


class FlightData():
    #This class is responsible for structuring the flight data.
    def __init__(self, flight_data: DataManager, flightsearch: FlightSearch):
        self.flight_data = flight_data
        self.flight_search = flightsearch

    def populate_iata(self):
        """Populating each IATA Code cell in our google sheet"""
        cities = self.flight_data.get_cities()
        for city in cities:
            city_data = self.flight_search.get_city_data(city=city["city"])
            iata_config = {
                "price": {
                    "iataCode": city_data["locations"][0]["code"]
                }
            }
            put_response = requests.put(url=f'{self.flight_data.get_url}/{city["id"]}', json=iata_config)
            put_response.raise_for_status()
            print(put_response.text)
