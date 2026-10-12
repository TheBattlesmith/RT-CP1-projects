# Roman Torres, period 1, Escape Room

game_on = True
places = [1, 2, 3 ]

while game_on == True:

    
    first_name = input("what is your first name. \n You can input nearly anything, just remember you'll have this name for the rest of the game: ").strip().title()

    last_name = input("what is your last name, \n you can input nearly anything, just remember you'll have this name for the rest of the game: ").strip().title()

    # split seperates characters into lists

    first_seperated = first_name.split()
    seperated = last_name.split()

    # join takes characters together

    fixed = "".join(seperated)
    last_fixed = "".join(first_seperated)


    full_name = last_fixed.title() + " " + fixed.title()

    print(f"\nHello, {full_name}, and welcome to the circus! \n\nIt's lovey here! only recently the sun has set, and your friends headed out. \nIt's your birthday though, and you figure that you might as well stay a while longer.\nAfter all, there are still three places you haven't visited yet!")

    while True:
        try:
            going = input("Which would you like to go to first? Please input a number\n1: look at the tiger.\n2: watch the strong man. \n3: go into the corn maze. ").lower().strip()
        except:
            print("that wasn't an option")