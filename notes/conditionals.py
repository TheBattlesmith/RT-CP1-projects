# RT, Conditionals notes 

# Conditional statement: a piece of code that makes a desicion based on a Boolean value

# If: runs a block of code only if its condition is true

# Else: runs a block of code if the if condition (and any elifs above it) was False. it's pretty much just, otherwise do this.

# White Space: tabbing over lines to place them into the if statement or any time a line ends with a colon
# order matters in conditionals, the code reads top to bottom. Start with the least likely outcome
# (if is_raining and If is_raining == True:) are the same


answer = input("are you passing the class? ")

passing = False

if answer == "yes":
    passing = True

else:
    print("sucker")

if passing == True:
    print("you are passing the class")


grade = 70

if grade >= 90:
    print("you've got an A!")
elif grade >= 70:
    print("You are passing!")
else:
    print("you're a failure!")

username = input("what's your username? ")

if bool(username):
    print("You didn't type it in!")
elif username == "JD":
    print("you are a teacher")
else:
    print("you're a student")