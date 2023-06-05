import requests
import json

api_key = "2b8aefcd7dc3bbe081e8fe045860bb4f"
base_url = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error occurred while fetching weather data.")
        return None

def get_temperature(city):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data["main"]["temp"]
    else:
        return None

def get_humidity(city):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data["main"]["humidity"]
    else:
        return None

def get_pressure(city):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data["main"]["pressure"]
    else:
        return None

def get_wind_speed(city):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data["wind"]["speed"]
    else:
        return None

def get_weather_description(city):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data["weather"][0]["description"]
    else:
        return None

def get_weather_icon(city):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data["weather"][0]["icon"]
    else:
        return None

city = input("Enter city name: ")
weather_data = get_weather(city)

if weather_data:
    print("Temperature:", get_temperature(city))
    print("Humidity:", get_humidity(city))
    print("Pressure:", get_pressure(city))
    print("Wind Speed:", get_wind_speed(city))
    print("Weather Description:", get_weather_description(city))
    print("Weather Icon:", get_weather_icon(city))
else:
    print("City Not found. Could not retrieve weather data.")


