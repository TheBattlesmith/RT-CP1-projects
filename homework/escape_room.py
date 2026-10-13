# Roman Torres, period 1, Escape Room
import random
import time
game_on = True
places = [1, 2, 3 ]

while game_on == True:
    win = False
    chase = False
    scr = False
    death = 0
    escape = [1,2]
    beans = random.randint(1,2)
    if beans == 1:
        monster = "tiger"
    if beans == 2:
        monster = "strong man"

    find_crow = 0
    scarecrow = random.randint(4,8)
    riddles = False
    SC_chances = 3 

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
                else:
                    break
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

    # MAZE DESCRIPTION

    print("You step onto the path leading deeper into the rows of seemingly endless corn.\n\n ")
    time.sleep(1)
    print("Then something odd happens...\n\n")
    time.sleep(1)
    print("The sounds from the circus behind you suddenly go quiet... you turn and realize that the entrance is gone, replaced by a wall of corn stalks...\n")
    print("Then the moon blinks... for a split second everything goes black, but then the light is back...\n\n but now it's red... the scarlet glow illuminates the corn and something else...\n\n")
    print(f"The {monster} stands only thirty feet from you, eyes glowing red as the moon... it looks at you and grins, revealing a row of sharp teeth.")

    while True:
        try:
            run = int(input("Will you run? \n1 for yes: \n2 for no: "))
            if run not in escape:
                raise TypeError("that wasn't an option")
            else:
                break
        except:
            print("You can't do that!")
        else:
            break
    while True:
        if run == 1:
            chase = True
            break
        else:
            print("Are you sure?")
            death += 1
            if death == 2:
                print(f"The {monster} charges... everything fades to black as the {monster} attacks... and you die.")
                break
            break

    while chase == True:
        try:
            turn = input("Quick! It’s an intersection! 1 for left 2 for right! ")
            if turn not in escape:
                raise TypeError("that wasn't an option")
            else:
                break
        except:
            print("You can't do that!")
        else:
            break
        find_crow += 1
        if find_crow == scarecrow:
            print(f"As you look over your shoulder, your foot snags on something in the darkness, and you fall, not onto dirt though… you realize you”ve fallen into a wooden, roofless room in the center of the corn maze, a door slams shut behind you, a small window in its center allowing you to see the {monster} bolt up to the door and begin ferociously pounding against it… the wood holds, but it won’t last forever. You need to find a way out of here!")
            print(f"You spot a second door at the far end of the room alongside a frightening scarecrow that hangs not three feet from it on a wooden pole.You walk cautiously to the door, trying the knob… \n\nIt’s LOCKED!!!!!!!!!! Then, out of the corner of your eye, you see the scarecrow twitch, you look up and find it now stares directly at you! \n\n“If you want to open my door,” it hisses, “you’ll have to play my game.\n\n")

            print(f"The {monster} slams ferociously into the door behind you, the wood beginning to crack! The scarecrow grins, “shall we play yes… or no…?")
            scr = True
            break



    while scr == True:
        try:
            hmm = input("Will you play the scarecrow's game? \n1 for yes: \n 2 for no: ")
            if hmm not in escape:
                raise TypeError("that wasn't an option")
            else:
                break
        except:
            print("You can't do that!")
        else:
            break

        if hmm == 1:
            riddles = True
            print("The scarecrow grins even wider, “very well… all I ask is that you answer my question with one word.")
        else:
            break

    while riddles == False:
        print(f"You stand, looking defiantly at the scarecrow, whose smile grows even wider.\n “very well, ” it whispers, flicking its wrist. \nThe door you’ve just come from unlocks, \nthe {monster} bolts in and lunges for you… everything suddenly goes black… as you die…")
        break


