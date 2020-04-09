#A program for drawing a colorful spiral
import turtle
from random import choice
turtle.setposition(0,0)
angle=40
distance=0.5
turtle.pencolor('black')
turtle.hideturtle()
for i in range(500):
    turtle.forward(distance)
    turtle.bgcolor(choice(['red','blue','cyan','green','pink','yellow']))
    turtle.left(angle)
    distance+=.5
