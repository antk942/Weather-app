import requests

from config import API_KEY

import utils

if __name__ == '__main__':
    units = utils.get_user_preference("Units.json")
    language = utils.get_user_preference("Languages.json")
    coords = utils.get_coordinatess()  # lat + lon

    url = f'https://api.openweathermap.org/data/2.5/weather?{coords}&units={units}&lang={language}&appid={API_KEY}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
