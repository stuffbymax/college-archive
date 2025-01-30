# image source:
# map.jpg: https://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
import turtle
import urllib.request
import json

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
iss_now = json.loads(response.read())

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
astros = json.loads(response.read())

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)


location = iss_now['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

iss.penup()
iss.goto(lat, lon)

num_people = turtle.Turtle()
num_people.penup()
num_people.hideturtle()
num_people.color('yellow')
num_people.goto(-175,-25)
num_people.write('people in space: ' + str(astros['number']))

num_name = turtle.Turtle()
num_name.penup()
num_name.hideturtle()
num_name.color('yellow')
num_name.goto(-175, -50) 

people = astros['people']
names = [] 
for p in people:
    names.append(p['name'])

num_name.write('Astronauts: ' + ', '.join(names), align='left')
