import logging
import os
import sys
from datetime import datetime
import requests
from dotenv import load_dotenv
from adapter.twilio_sms_sender import send_sms

# Loading environment variables from .env file
load_dotenv()

# Logger config


def parse_weather_info(data):
    temp_c = data['current']['temp_c']
    feels_like_temp = data['current']['feelslike_c']
    condition = data['current']['condition']['text']
    wind_speed_kmh = data['current']['wind_kph']
    return f"Today it is  {condition}. Temperature is {temp_c}°C. Feels like {feels_like_temp}°C. Wind: {wind_speed_kmh}km/h."


def weather_api(city):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    current_weather_endpoint = "/current.json"
    params = {
        'key': os.getenv('WEATHER_API_KEY'),
        'q': city
    }
    response = requests.get(
        url=base_url + current_weather_endpoint,
        params=params
    )

    if response.status_code != 200:
        print(f'Weather API response code: {response.status_code}')
        sys.exit(0)
    return response.json()


def get_city():
    args = sys.argv
    if args.__sizeof__() == 1:
        return args[1]
    else:
        return 'Warsaw'


if __name__ == '__main__':
    print("Started")
    input_city = get_city()
    data = weather_api(input_city)
    weather_info = parse_weather_info(data)
    send_sms(weather_info)
    print("Finished")
