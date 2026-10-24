# Roman Torres, period 1, Fix the Game





import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        while True:
            try:
                guess = int(input("Guess a number between 1 and 20: "))
            except:
                print("your input must be an integer:")
            else:
                break                          # Stupid proofing
        guesses = guesses + 1

        if guess == secret_number: # SyntaxError - colon added
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)



print("\n--- Game Over ---")
print("Your guesses per round: " + str(scores)) # TypeError - converted scores to a string


total = 0
for score in scores:
    # LogicError - total was being reset to zero with every runthrough of the code
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(round(average, 2))) # rounded to two decimal places

best_round = scores[0]
for i in range(1, len(scores)): # LogicError - we need this to run a number of times equal to the length of the scores list in order to get the actuall number
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")