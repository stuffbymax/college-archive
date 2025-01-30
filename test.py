# image source:
# map.jpg: https://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
import turtle
import urllib.request
import json

screen = turtle.Screen()
screen.setup(720, 360)
screen.bgpic('map.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
astros = json.loads(response.read())


num_people = turtle.Turtle()
num_people = turtle.Turtle()
num_people.penup()
num_people.hideturtle()
num_people.color('yellow')
num_people.goto(-175,-25)
num_people.write('people in space: ' + str(astros['number']))
