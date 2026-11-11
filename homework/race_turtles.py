# Roman Torres, Period 1, Turtle race

import random

import turtle as t


# Function for placing turtles into their starting positions
def start(turtle, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.teleport(-300, y)
    turtle.pendown()
    turtle.showturtle()

# Function for selecting the differing colors for each turtle
def feature(turtle, color):
    turtle.shape("turtle")
    turtle.color(color)
    turtle.pencolor("black")


    
# Function for turtle movement in each leg of the race
def move(turtle):
    distance = random.randint(5,20)
    for i in range(distance):
        turtle.tilt(40)
        turtle.forward(5)
        turtle.tilt(-40)
   
# Function for finding whether a turtle has won
def check (turtle, n, winner):
    if turtle.position() >= (300, n):
        turtle.write("Hooray! I WON!!!!")   
        turtle.right(360)
        print(f"{winner}, WINS!!!")
        return False
    else:
        return True

        

        
                    

no_win = True

# Setup of the finish line
t_map = t.Turtle()
t_map.pensize(10)
t_map.hideturtle()
t_map.penup()
t_map.goto(300, 250)
t_map.right(90)
t_map.pendown()
t_map.forward(500)


# Setup of the seperate turtles colors, and positions
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



# Race loop
while no_win == True:

    move(t_red)
    no_win = check(t_red, 200, "RED")
    

    move(t_orange)
    no_win = check(t_orange, 100, "ORANGE")

    move(t_purple)
    no_win = check(t_purple, 0, "PURPLE")

    move(t_green)
    no_win = check(t_green, -100, "GREEN")

    move(t_blue)
    no_win = check(t_blue, -200, "BLUE")

    







# Keeps the page open until clicked
t.exitonclick()
