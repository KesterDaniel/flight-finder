import os

from flight_search import FlightSearch
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

context = ssl.create_default_context()


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self, flightsearch: FlightSearch):
        self.flight_search = flightsearch
        self.password = os.getenv("MY_PASSWORD")
        self.email_address = "kesterdaniel401@gmail.com"
        self.cheap_flights = flightsearch.cheap_flights

    def send_mail(self):
        """Send mail containing cheap flights data"""
        if len(self.cheap_flights) != 0:

            # create message
            subject = "Low Price Alert!"
            msg = MIMEMultipart()
            msg["From"] = self.email_address
            msg["To"] = "kesterdan17@gmail.com"
            msg["Subject"] = subject

            # create HTML message body
            html = "<html><body>"
            for flight in self.cheap_flights:
                html += f"<h3>Flight from {flight['departure_city']}-{flight['departure_airport_code']} to {flight['arrival_city']}-{flight['arrival_airport_code']}</h3>"
                html += f"<ul>" \
                        f"<li>Price: {flight['price']}</li>" \
                        f"<li>Outbound Date: {flight['outbound_date']}</li>" \
                        f"<li>Inbound Date: {flight['inbound_date']}</li>" \
                        f"</ul>"
                html += "<br>"
            html += "</body></html>"

            msg.attach(MIMEText(html, "html"))

            # send email
            with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
                connection.login(user=self.email_address, password=self.password)
                connection.sendmail(
                    from_addr=self.email_address,
                    to_addrs="kesterdan17@gmail.com",
                    msg=msg.as_string()
                )

