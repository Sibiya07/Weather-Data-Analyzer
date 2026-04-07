import requests
from app.config import API_KEY

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print("Error fetching data:", data)
        return None

    return data