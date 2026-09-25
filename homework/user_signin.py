# Roman Torres, User Sign In, period 1

import random

user_name = ["Miss. LaRose", "roman.torres"]






while True:

    try:
        username = input("Please input your username: ")
        if username not in user_name:
            raise TypeError ("That is incorrect. Please input a valid username.")

    except:
        print("that is incorrect. Please try again.")
    else:
        break

if username == "Miss. LaRose":
    password_answer = "Beans!"

if username == "roman.torres":
    password_answer = "Meatloaf!"

while True:

    password = input("Please input your password ")
    
    if password_answer == password:
        print(F"Welcome, {username}.")
        program = random.randint(1,2)
        break

    else:
        print("That is an invalid passcode.") 

