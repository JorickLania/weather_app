## Imports
import requests
import os
from dotenv import load_dotenv

## Load environment variables
load_dotenv()

## Get-Weather-Function
def get_current_weather():
    print("\n*** Let's take a look at the current weather! ***\n")

    city = input("\n Please specify a city: \n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #print("Sending request to OpenWeather with request_url \n", request_url)

    weather_data = requests.get(request_url).json()
    print(weather_data)

get_current_weather()