import requests
from datetime import date
from dateutil.relativedelta import relativedelta

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flightdata = DataManager()
flightsearch = FlightSearch(flightdata)

flightsearch.get_flight_data()

# structure_data = FlightData(flightdata, flightsearch)
# Effecting changing the IATA Code in google sheet
# structure_data.populate_iata()



