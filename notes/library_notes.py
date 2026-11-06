#Library: a collection of pre-written code (mostly functions) that you can bring into your own program instead of writing it yourself

#Import: the statement that brings a library into your program. It goes at the top of your file, for example import math.

#Built-in function: a function that comes with Python and is ready to use, like print(), input(), and len(). No import is needed.

#Library function: a function that lives inside a library. You have to import the library first, then call it with the library's name, like math.sqrt(16).

#User-defined function: a function you write yourself with def

#Argument: a value you give to a function when you call it, like the 16 in math.sqrt(16)

#Void return: a function that does its job but doesn't hand back a value (it returns None). Turtle's forward() is an example.

#Why use libraries? They save time, they are already tested, and they let you do big things (graphics, math, randomness) with very little code

#Turtle: a library that lets you draw by giving commands to a "turtle" that moves around the screen


# import method - - - Aliasing, not obvious what t is though so not as good, but you can call any 
import turtle as t

t.showturtle()
t.shape("turtle")
t.shapesize(3)
t.tilt(270)
t.color("green")
t.width(10)
t.speed(5)
t.penup()
t.hideturtle()
t.backward(500)
t.showturtle()
t.pendown()
t.write("You brought this on yourself!")

t.penup()
t.hideturtle()
t.goto(100, 50)
t.showturtle()
t.pendown()
t.write("You let the mosters out!")

t.penup()
t.hideturtle()
t.goto(0, 0)
t.showturtle()
t.pendown()

"""t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)
t.right(90)
t.forward(250)

t.forward(20)
t.circle(200)
t.right(720)"""
#keeps the window open until you click it
t.exitonclick()

# returns turtle to position (0,0)
t.home()
