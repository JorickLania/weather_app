## Imports
import requests
import os
from dotenv import load_dotenv
from pprint import pprint

## Load environment variables
load_dotenv()

## Get-Weather-Function
def get_current_weather(show_request=False, units='metric'):
    '''Function requests weather data from OpenWeather.org based on user input city.
       Input:
       show_request    bool    : If True, prints full request url back to user. Default is False.
       units           string  : Units of the returned weather data. Options are 'metric', 'imperial'. Default is 'metric'.
    '''
    print("\n*** Let's take a look at the current weather! ***\n")

    city = input("\n Please specify a city: \n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units={units}'
    if show_request is True:
        print("Sending request to OpenWeather with request_url \n", request_url)

    if units=='metric':
        T_unit = 'C'
    elif units=='imperial':
        T_unit = 'F'    

    weather_data = requests.get(request_url).json()
    print(f'Current Weather for {weather_data["name"]}:')
    print(f'Current temperature: {weather_data["main"]["temp"]} {T_unit}, feels like {weather_data["main"]["feels_like"]} {T_unit}')
    print(f'Current humidity: {weather_data["main"]["humidity"]}')
    print(f'Weather info for today: {weather_data["weather"][0]["description"]}.')

if __name__ == "__main__":
    get_current_weather()