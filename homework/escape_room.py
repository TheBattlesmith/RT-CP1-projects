# Roman Torres, period 1, Escape Room

game_on = True
places = [1, 2, 3 ]

while game_on == True:

    # CHOOSING NAME CODE
    first_name = input("what is your first name. \n You can input nearly anything, just remember you'll have this name for the rest of the game: ").strip().title()

    last_name = input("what is your last name, \n you can input nearly anything, just remember you'll have this name for the rest of the game: ").strip().title()


    first_seperated = first_name.split()
    seperated = last_name.split()

    

    fixed = "".join(seperated)
    last_fixed = "".join(first_seperated)


    full_name = last_fixed.title() + " " + fixed.title()

    print(f"\nHello, {full_name}, and welcome to the circus! \n\nIt's lovey here! only recently the sun has set, and your friends headed out. \nIt's your birthday though, and you figure that you might as well stay a while longer.\nAfter all, there are still three places you haven't visited yet!")

    # CHOOSING MAZE CODE
    while True:
        while True:
            try:
                going = int(input("Which would you like to go to first? Please input a number\n1: look at the tiger.\n2: watch the strong man. \n3: go into the corn maze. "))
                if going not in places:
                    raise TypeError("That wasn't an option.")
            except:
                print("That wasn't an option.")
            else:
                break
        if going == 3:
            print("A light fog drifts over the seemingly infinite cornstalks.\n\nYou take a deep breath, and enter.")
            break
    
        elif going == 2:
            print("\nYou gasp in amazement as the strong man heaves a horse over his head.\n")
        elif going == 1:
            print("\nThe massive tiger stalks through the ring, a large blindfold over its eyes as it follows its master by smell.\n")
        else:
            print("Wait, how did that number pass?")
    