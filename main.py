# import requests
#
# api_key = "a258cf529b6e0daa1be39637fe53f01e"
# my_lat = -37.813629
# my_lon = 144.963058
#
#
# parameter = {
#     "lat": my_lat,
#     "Lon": my_lon,
#     "appid": api_key,
#     "exclude": "daily",
#
# }
# parameter = {
#     "lat": my_lat,
#     "Lon": my_lon,
#     "appid": api_key,
#
#
# }
#
# api_key = "a258cf529b6e0daa1be39637fe53f01e"
# my_lat = -37.813629
# my_lon = 144.963058
#
# parameter = {
#     "lat": my_lat,
#     "lon": my_lon,
#     "appid": api_key,
# }
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameter)
#
# # response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)
# response.raise_for_status()
# data = response.json()
# print(response.status_code)
# print(data)
#

import requests
import os
from twilio.rest import Client

account_sid = 'ACeb1aedeab28d3478f63a7565d493ec66'
auth_token = '2b8e0d4d7bd27f779d360f9f359e81f4'

api_key = "a258cf529b6e0daa1be39637fe53f01e"
my_lat = -37.813629
my_lon = 144.963058

parameter = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily",

}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
print(response.status_code)
print(weather_data)
for i in range(0,13):
    weather_id = weather_data['hourly'][i]['weather'][0]['id']
    if weather_id > 800:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+14705169436',
            to='+61470557910'
        )

        print(message.status)

