import requests

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flightsearch = FlightSearch()
flightdata = DataManager()

structure_data = FlightData(flightdata, flightsearch)

# Effecting changing the IATA Code in google sheet
structure_data.populate_iata()

