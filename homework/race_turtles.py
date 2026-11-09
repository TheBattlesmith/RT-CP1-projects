# Roman Torres, Period 1, Turtle race

import random

import turtle as t

def start(turtle, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.teleport(-300, y)
    turtle.pendown()
    turtle.showturtle()

def feature(turtle, color):
    turtle.shape("turtle")
    turtle.color(color)
    turtle.pencolor("black")


    

def move(turtle):
    distance = random.randint(10,20)
    for i in range(distance):
        turtle.tilt(-20)
        turtle.forward(5)
        turtle.tilt(20)



t_map = t.Turtle()
t_map.pensize(10)
t_map.hideturtle()
t_map.penup()
t_map.goto(300, 250)
t_map.right(90)
t_map.pendown()
t_map.forward(500)

t_red = t.Turtle()
start(t_red, 200)
feature(t_red, "red" )


t_orange = t.Turtle()
start(t_orange, 100)
feature(t_orange, "orange")

t_purple = t.Turtle()
start(t_purple, 0)
feature(t_purple, "purple")

t_green = t.Turtle()
start(t_green, -100)
feature(t_green, "green")

t_blue = t.Turtle()
start(t_blue, -200)
feature(t_blue, "blue")

while True:

    move(t_red)
    move(t_orange)
    move(t_purple)
    move(t_green)
    move(t_blue)







t.exitonclick()
