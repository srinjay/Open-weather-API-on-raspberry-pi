from requests import get
from datetime import datetime,timedelta
from json import loads
from pprint import pprint

KEY='7706d31a07bf59ab15bbc4fedde65dbe'

def get_city_id():
    with open('city.list.json')as f:
        data=[loads(line) for line in f]
    city=input('wHICH CITY ARE YOU TRAVELLING TO?')
    city_id=False
    for item in data:
        if item["name"] == city:
            answer=input("Is this in" +item["country"])
            if answer == 'y':
                city_id= item["_id"]
            break

    if not city_id:
        print("sorry,location unavailable!")
        return city_id

def get_weather_data(city_id):
    weather_data=get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}.format(city_id,KEY)')
    return weather_data.json()


def get_arrival
