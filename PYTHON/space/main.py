import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
astros = json.loads(response.read())
print(astros)

people = astros['people']

for p in people:
    print(p['name'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
iss_now = json.loads(response.read())

location = iss_now['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)
