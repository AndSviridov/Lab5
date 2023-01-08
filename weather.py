from requests import get

API_key = '3719472b99c7a6d44e68661e83070d03' # add your API key

def get_geo(city_name):
    r = get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}')
    return r.json()[0]

def get_weather(lat, lon):
    r = get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}')
    return r.json()

name = input('Enter city name: ')
geo = get_geo(name)

print(f"{geo['name']},", f"{geo['country']},", geo['lat'], geo['lon'])

data = get_weather(geo['lat'], geo['lon'])

main = data['main']
weather = data['weather']

print(weather[0]['description'])
print(f"temp {main['temp']}, feels like {main['feels_like']}")
print(f"pressure {main['pressure']}, humidity {main['humidity']}")

