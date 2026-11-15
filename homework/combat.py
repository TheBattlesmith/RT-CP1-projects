# Roman Torres, period 1, Combat Program


import random

def classes (which):
   if which == 1:
       return "sorcerer"
   if which == 2:
       return "assassin"
   if which == 3:
       return "knight"
   if which == 4:
       return "priest"
# difficulty/monster choice function
def difficulty(difficult):
   if difficult == 1:
       monster = "wolf"
   if difficult == 2:
       monster = "bear"
   if difficult == 3:
       monster = "dark knight"
   return monster




# Chance function


def d20():
   roll = random.randint(1,20)
   return roll


# monster’s turn


def m_turn (type, php, matk, ac):
   if type == "wolf":
       attack = d20() +1
       if attack >= ac:
           php = random.randint(1, 8) + matk
           return php
       else:
              return 0
   if type == "bear":
       attack = d20() + 2
       if attack >= ac:
           php = random.randint(1, 10) + matk
           return php
       else:
              return 0
   if type == "dark knight":
       attack = d20() + 4
       if attack >= ac:
           php = random.randint(1, 12) + matk
           return php
       else:
              return 0


# Player’s turn based on class chosen


def p_turn(p_class):
   if p_class == "sorcerer":
       while True:
           try:
               move = int(input("\n\nWhat spell would you like to use?\n(1)Chaotic inferno(A mote of flame flies from your hand… you’re not sure how strong it’ll be though)\n(2)Shield of Change(A glowing defensive sigil appears in the air before you… most of the time)\n(3)Life Begotten(you’re not completely sure what this does, but you do know that you feel good after)\n(4)Escape(No magic, you’re just being a pansy)\n\n"))
               if move not in available:
                   raise TypeError("that wasn’t an option.")
           except:
               print("That wasn’t an option.")
           else:
               break


   if p_class == "assassin":
       while True:
           try:
               move = int(input("\n\nWhich technique will you employ?\n(1)Death Strike(You attack your opponent where they’re weakest dealing huge amounts of damage)\n(2)Evade(For the next few seconds, you slip duck and weave under all attacks… most of the time)\n(3)Health Potion(Have a quick drink and get back to fighting more energized than before)\n(4)Run Away(Aaaaaaaaaah!!!)\n\n"))
               if move not in available:
                   raise TypeError("That wasn’t an option.")
           except:
               print("That wasn’t an option.")
           else:
               break




   if p_class == "knight":
       while True:
           try:
               move = int(input("\n\nWhich way shall your steel fly?\n(1)Attack(The basic combination taught to all knights for the reason of combat)\n(2)Parry(Your shield shoots forward, attempting to bash away incoming attacks)\n(3)Mipha’s grace(A special healing technique known only to you and some fish)\n(4)Flee(you’ll bring dishonor to yourself)\n\n"))
               if move not in available:
                   raise TypeError("That wasn’t an option.")
           except:
               print("That wasn’t an option.")
           else:
               break


   if p_class == "priest":
       while True:
           try:
               move = int(input("\n\nHow will you invoke your god?\n(1)Divine flame(A static point of fire blasts through the air dealing a set amount of damage each time)\n(2)Faith’s shield(You close your eyes as only the hand of your god protects you, although sometimes you catch em with their pants down and they don’t get there in time)\n(3)Healing light(divine energy suffuses your body mending wounds)\n(4)Pee your pants(This isn’t exactly a divine spell but it wouldn’t be the first time\n\n"))
               if move not in available:
                   raise TypeError("That wasn’t an option.")
           except:
               print("That wasn’t an option.")
           else:
               break
   return move






# The effects of the player’s choice of move


def move_effect(decision,p_class, mac ):
    if p_class == "sorcerer":
        if decision == 1:
            fire = random.randint(1, 30)
            return fire
        elif decision == 2:
            shield = random.randint(1, 10)
            return shield
        elif decision == 3:
            heal = random.randint(1, 10)
            return heal
        else:
            done = "finished"
            return done
    if p_class == "assassin":
        if decision == 1:
            roll = d20() + 5
            if roll >= mac:
                fire = random.randint(20, 25)
                return fire
            else:
                return 0
        elif decision == 2:
            shield = random.randint(5, 9)
            return shield
        elif decision == 3:
            heal = random.randint(1, 5)
            return heal
        else:
            done = "finished"
            return done

    if p_class == "knight":
        if decision == 1:
            roll = d20() + 6
            if roll >= mac:
                fire = random.randint(10, 15)
                return fire
            else:
                return 0
        elif decision == 2:
            shield = random.randint(1, 10)
            return shield
        elif decision == 3:
            heal = random.randint(5, 10)
            return heal
        else:
            done = "finished"
            return done
    if p_class == "priest":
        if decision == 1:
            roll = d20() + 3
            if roll >= mac:
                fire = random.randint(5, 10)
                return fire
            else:
                return 0
        elif decision == 2:
            shield = random.randint(1, 4)
            return shield
        elif decision == 3:
            heal = random.randint(10, 15)
            return heal
        else:
            done = "finished"
            return done




# function of possible classes to choose




# showing abilities based on class


def abilities ():
  
   if p_class == "sorcerer":
       abilities = ["Chaotic inferno", "Shield of Change", "Life Begotten", "Escape"]
     
   if p_class == "assassin":
       abilities = ["Death Strike", "Evade", "Health Potion", "Run Away"]
     
   if p_class == "knight":
       abilities = ["Attack", "Parry", "Mipha's Grace", "Flee"]
      
   if p_class == "priest":
       abilities = ["Divine Flame", "Faith's Shield", "Healing Light", "Pee Your Pants"]
   return abilities
  
         
# Stupid proofing lists       


available = [1,2,3,4]
options = [1,2,3]
done = [1,2]

j = True



# Asking user what class they want to be

while j == True:
    while True:
        try:
            choice = int(input("Which class do you choose to be? please input a number.\nSorcerer(1)\nAssassin(2)\nKnight(3)\nPriest(4)\n"))
            if choice not in available:
                raise TypeError("That wasn't an option.")
        except:
            print("That wasn't an option.")
        else:
            break
    p_class = classes(choice)
    powers = abilities()




    # Asking user what difficulty they want


    while True:
        try:
            difficult = int(input("\nWhat difficulty — 1, 2, or 3: "))
            if difficult not in options:
                raise TypeError("that wasn’t an option.")
        except:
            print("That wasn’t an option")
        else:
            break


    # Defining monster stats


    monster = difficulty(difficult)


    if monster == "wolf":
        mhp = 25
        mac = 10
        matk = 1
    if monster == "bear":
        mhp = 35
        mac = 14
        matk = 3
    if monster == "dark knight":
        mhp = 50
        mac = 18
        matk = 8




    # Telling user what they’ve chosen and their abilities, and what monster you’ll be fighting based on your chosen difficulty
    
    print(f"You are a {p_class} and your abilities are." )
    for i in powers:
        print(i)


    print(f"You are fighting a {monster}!")
    chance = random.randint(1,2)



    # Defining user hit points based on class


    if p_class == "sorcerer":
        php = 30
        attack = 3
    if p_class == "assassin":
        php = 25
        attack = 10
    if p_class == "knight":
        php = 45
        attack = 8
    if p_class == "priest":
        php = 25
        attack = 0


    # Combat loop

    if chance == 2:
        while mhp > 0 and php > 0:

            # Redefining ac to ensure the defensive ability doesn’t stack
            if p_class == "sorcerer":
                ac = 13
            if p_class == "assassin":
                ac = 15
            if p_class == "knight":
                ac = 17
            if p_class == "priest":
                ac = 10

            decision = p_turn(p_class)
            you = move_effect(decision, p_class, mac)
            if decision == 1:
                mhp -= you
            elif decision == 2:
                ac += you
            elif decision == 3:
                php += you
            else:
                break

            print(f"\nYour foe is at {mhp} hit points.\n")

            enemy = m_turn(monster, php, matk, ac)
            php -= enemy
            print(f"\nYou are at {php} hit points.\n")

    if chance == 1:
        while mhp > 0 and php > 0:

            enemy = m_turn(monster, php, matk, ac)
            php -= enemy
            print(f"\nYour enemy attacked and dealt {enemy} damage!\n")
            print(f"\nYou are at {php} hit points.\n")

            # Redefining ac to ensure the defensive ability doesn’t stack
            if p_class == "sorcerer":
                ac = 13
            if p_class == "assassin":
                ac = 15
            if p_class == "knight":
                ac = 17
            if p_class == "priest":
                ac = 10

            decision = p_turn(p_class)
            you = move_effect(decision, p_class, mac)
            if decision == 1:
                mhp -= you
            elif decision == 2:
                ac += you
            elif decision == 3:
                php += you
            else:
                break

            print(f"\nYour foe is at {mhp} hit points.\n")
            print(f"\nYou are at {php} hit points.\n")
            print(f"\nYour AC is {ac}.\n")




    if mhp <= 0:
        print(f"\nYou have defeated the {monster}!\n")
    elif php <= 0:
        print(f"\nYou died!\n")
    else:
        print(f"\nYou ran away from the {monster}... Coward!\n")

    while True:
        try:
            again = int(input("Would you like to play again?\n(1)Yes\n(2)No\n"))
            if again not in done:
                raise TypeError("That wasn’t an option.")
        except:
            print("That wasn’t an option.")
        else:
            break

    if again == 1:
        print("Excellent!")
    if again == 2:
        print("Goodbye!")
        j = False