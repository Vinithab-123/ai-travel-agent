from langchain.tools import tool
import requests

@tool
def get_weather(city: str) -> dict:
    """
    Fetch weather data using Open-Meteo API
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 15.2993,
        "longitude": 74.1240,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "temperature": f"{data['current_weather']['temperature']}°C",
        "windspeed": f"{data['current_weather']['windspeed']} km/h"
    }
