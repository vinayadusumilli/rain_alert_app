import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MY_WEATHER_API_KEY")  # Own API key from "https://openweathermap.org/" weather api provider
LATITUDE = os.getenv("MY_LATITUDE")  # Latitude "https://www.latlong.net/"
LONGITUDE = os.getenv("MY_LONGITUDE")  # Longitude

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,  # cnt parameter to get four weather response with three hours interval
}


def is_raining() -> bool:
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    for interval in weather_data["list"]:
        code = interval["weather"][0]["id"]
        if 500 <= code <= 700:  # Go through "https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2"
            # to understand about api weather codes
            return True
        else:
            return False


if is_raining():
    print("It's rain today, don't forget to bring umbrella☔️")
