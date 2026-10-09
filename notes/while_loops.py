# While loops

# Iterator keeps track of our current iteration of our loop

# for loops repeat for everything in a list
# while loops will continue until a certain condition is met

import random
import time

goose = random.randint(1, 20)

#pt.1 Start point
duck = 1


#pt.2 end point< this is a boolean, code will run until it is false
while goose > duck:
    print("duck...")
    time.sleep(0.5)
    #pt.3 incrementor: it is used to change your iterator
    duck += 1
    if duck == 15:
        print("Game Over")
        break
# an else in a while will only run when the code above is false. using break makes the else not run.
else:
    print("Goose!!!!!!!!")


count = 1

while count <= 30:
    print(count)
    time.sleep(0.1)
    count += 1
guesses = 0


correct = random.randint(1,101)

while True:
    while True:
        try:
            guess = int(input("what is your guess 1-100? "))
            if guess < 0 or guess > 100:
                print("You should read instructions:")
                continue
        except:
            print("That's not a number:")
        else:
            break

    guesses += 1

    if guess == correct:
        print("You got it!")
        print(f"you guessed: {guesses} times")
        break
    elif guess > correct:
        print("Ohh, to high:")
    elif guess < correct:
        print("Nope, to low")
    else:
        print("How did you get there, that's wrong.")

    
    