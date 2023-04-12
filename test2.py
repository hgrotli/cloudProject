import json
import requests
import sys


API_LINK = 'http://127.0.0.1:5000/contacts'


response = requests.get(API_LINK)
print(response)
data = response.json()
# print(json.dumps(data, indent=2))

with open('our_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)


# open('data.json', 'w').write(json.dumps(requests.get('https://www.7timer.info/bin/astro.php?lon=60.8&lat=10.7&ac=0&unit=metric&output=json&tzshift=0').json(), indent=4))



'''
def get_weather(city):
    try:
        response = requests.get(API_LINK)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.ConnectionError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.Timeout as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)

    data = response.json()

    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    return weather, temperature, pressure, humidity, wind_speed
'''
