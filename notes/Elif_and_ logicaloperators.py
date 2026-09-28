# Roman Torres Elif and Logical operators notes

# Logical operators:  and checks if both are true, or checks if one or the other is true, not flips a boolean to its opposite, pass a placeholder statement that does nothing, used when python requires a line of code but you don't want anything to happen yet.

#in an if elif else chain starts at the top and continues till it finds something true


# one line conditionals example

age = 70

adult = True if age >= 18 else False

print(f"You are an adult: {adult}")

# All conditionals begin with an if. an else also marks the end of a conditional. Elifs expand a conditional

if age >= 18:
    print("you're an adult.")
elif age >= 16:
    print("you can drive!")
else:
    print("You're a minor. go to school.")





win = True
hp = 0

if win or hp < 1:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost!")

else:
    print("the game is still going")