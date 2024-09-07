import requests
import os

api_key = "41cb9da3d805141f5d00f3c73dc64c8b"# os.getenv("WEATHER_API_KEY")
MY_LAT = 51.507351
MY_LON = -0.127758

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
for interval in weather_data["list"]:
    code = interval["weather"][0]["id"]
    print(code)
    if 500 <= code <= 700:
        print("It's raining")