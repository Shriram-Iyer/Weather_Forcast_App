import os
import requests
from dotenv import load_dotenv

load_dotenv()
APIkey = os.getenv('API_KEY')


def get_data(place,forecast_day):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list'][:8*forecast_day]
    return filter_data

if __name__ == "__main__":
    print(get_data("Mumbai",5))
