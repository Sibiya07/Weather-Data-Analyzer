from app.api.weather_api import fetch_weather
from app.repository.weather_repo import save_weather
from datetime import datetime

def collect_weather(city):
    try:
        data = fetch_weather(city)

        if data is None:
            return None, None

        temp = data['main']['temp']
        humidity = data['main']['humidity']

        save_weather([datetime.now(), temp, humidity])

        return temp, humidity

    except Exception as e:
        print("Error collecting weather:", e)
        return None, None