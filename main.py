from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

flightdata = DataManager()
flightsearch = FlightSearch(flightdata)
notify_me = NotificationManager(flightsearch)


flightsearch.get_flight_data()
notify_me.send_mail()






