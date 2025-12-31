
import requests
from crewai.tools import tool

class WeatherForecast():
    def __init__(self,description:str,temperature:float):
        self.description=description
        self.temperature=temperature

@tool("Weather forecast tool")
def get_weather_forecast()->WeatherForecast:
    """
    Return weather forecast for city jhansi.
    
    :return: Weather info.
    :rtype: WeatherForecast
    """
    url="https://api.openweathermap.org/data/2.5/weather"
    api_key="8d718bff47247bbfc5d743942090aa14"

    params={
        'q':'Jhansi',
        'appid':api_key,
        'units':'metric'
    }

    response=requests.get(url,params=params)
    result=response.json()

    return WeatherForecast(
        description=result["weather"][0]["description"].capitalize(),
        temperature=result["main"]["temp"]
    )

#forecast=get_weather_forecast()
#print(forecast.description,forecast.temperature)