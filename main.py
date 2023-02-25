import requests


from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flightdata = DataManager()
flightsearch = FlightSearch(flightdata)

# flightsearch.get_flight_data()





