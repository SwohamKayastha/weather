from dotenv import load_dotenv
import os
from requests import get, post
import json


load_dotenv()

api_key = os.getenv("API_KEY")


def get_latitude(api_key, city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    result = get(url)
    json_result = json.loads(result.content)[0]["lat"]
    return json_result



def get_longitude(api_key, city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    result = get(url)
    json_result = json.loads(result.content)[0]["lon"]
    return json_result


def get_current_weather(api_key, city_lat, city_lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}"
    result = get(url)
    json_result = result.json()
    weather = json_result.get('weather',{})
    return weather


def get_temperature(api_key, city_lat, city_lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}"
    result = get(url)
    json_result = result.json()
    main = json_result.get('main',{})
    return main



city_name = input("Enter the City Name: ")
city_latitude = get_latitude(api_key, city_name)
city_longitude = get_longitude(api_key, city_name)
weather = get_current_weather(api_key, city_latitude, city_longitude)
main = get_temperature(api_key, city_latitude, city_longitude)


def temp_conversion(K):
    C:float = K - 273.15
    return C

temp_c = temp_conversion(main['temp'])
temp_min_c = temp_conversion(main['temp_min'])
temp_max_c = temp_conversion(main['temp_max'])
temp_feels_c = temp_conversion(main['feels_like'])

print(f"Data : {city_latitude} & {city_longitude}")

print(f"Weather : {weather[0]['main']}")

print(f"JSON Format - main: {main}")
print(f"Temperature: {temp_c}")
print(f"Minimum Temperature: {temp_min_c}  &  Maximum Temperature: {temp_max_c}")
print(f"Feels like - {temp_feels_c}")