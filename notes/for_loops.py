# iteration - going through a collection of items one at a time, repeating the same action for each one
# For loop - a loop that repeats code once for each item in a sequence (like a list) - used when you know what your looping over


# Iterator variable - the variable that holds the current item during each pass through the loop. commonly named i, but can (and often should) be named something more descriptive like color when looping over a list of colors.

#repetition - running the same block of code more than once - loops are how programs repeat actions without copying and pasting the same code over and over.

# Met condition - when a loop's condition evaluates to true allowing it to continue or begin another pass.

# failed condition - when the loops condition evaluates to false, which is what causes the loop to stop.

#Exit condition - the condition that determines when a loop stops running - for a for loop, this is simply running out of items to iterate over.

# for (singular) in (plural) - lists should always be plural.

import time



siblings = {"Roman", "Meat", "Beans"}

for sibling in siblings:
    print(f"Good Morning {sibling}!")





grades = [100, 98, 76, 89, 84, 200, 2]

average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added.")

average = average / len(grades)
print(f"The average grade is: {average:.2f}")


# Range builds a list for you, the number inputed tells the code where to stop, the two at the end makes it count by twos.

# to prevent the print statement from starting a new line, print(name, end="")

for i in range(2, 21, 2):
    print(i)
    time.sleep(0.75)
for i in range(20, 0, -1):
    print(i)
    time.sleep(0.75)
    if i == 12:
        print("Wait, it's lunch time.")
        break

    print("You are insane!")