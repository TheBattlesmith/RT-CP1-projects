# Roman Torres, period 1, Combat Program

"""import random

def classes (which):
    if which == 1:
        return "sorcerer"
    if which == 2:
        return "assassin"
    if which == 3:
        return "knight"
    if which == 4:
        return "priest"
    


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
    
def AC():
    if p_class == "sorcerer":
        ac = random.randint(10, 13)
    if p_class == "assassin":
        ac = random.randint(15, 17)
    if p_class == "knight":
        ac = random.randint(16, 18)
    if p_class == "priest":
        ac = random.randint(9, 12)

    return ac        

        

available = [1,2,3,4]

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
ac = AC()

print(f"You are a {p_class} and your abilities are." )
for i in powers:
    print(i)
    """

import random

def d20():

	roll = random.randint(1,20)
	return roll

def m_turn (type):
	if type == "wolf":
		attack = d20() + matk
		if attack >= ac:
			php -= random.randint(1, 8) + matk
			return php
	if type == "bear":
		attack = d20() + matk
		if attack >= ac:
			php -= random.randint(1, 10) + matk
			return php
	if type == "dark knight":
		attack = d20() + matk
		if attack >= ac:
			php -= random.randint(1, 12) + matk
			return php

def p_turn(p_class):
	if p_class == "sorcerer":
		while True:
			try: 
				move = int(input("What spell would you like to use?\n(1)Chaotic inferno(A mote of flame flies from your hand… you’re not sure how strong it’ll be though)\n(2)Shield of Change(A glowing defensive sigil appears in the air before you… most of the time)\n(3)Life Begotten(you’re not completely sure what this does, but you do know that you feel good after)\n(4)Escape(No magic, you’re just being a pansy)"))
				if move not in available:
					raise TypeError("that wasn’t an option.")
			except:
				print("That wasn’t an option.")
			else:
				break

	if p_class == "assassin":
		while True:
			try:
				move = int(input("Which technique will you employ?\n(1)Death Strike(You attack your opponent where they’re weakest dealing huge amounts of damage)\n(2)Evade(For the next few seconds, you slip duck and weave under all attacks… most of the time)\n(3)Health Potion(Have a quick drink and get back to fighting more energized than before)\n(4)Run Away(Aaaaaaaaaah!!!)"))
				if move not in available:
					raise TypeError("That wasn’t an option.")
			except:
				print("That wasn’t an option.")
			else:
				break


	if p_class == "knight":
		while True:
			try:
				move = int(input("Which way shall your steel fly?\n(1)Attack(The basic combination taught to all knights for the reason of combat)\n(2)Parry(Your shield shoots forward, attempting to bash away incoming attacks)\n(3)Mipha’s grace(A special healing technique known only to you and some fish)\n(4)Flee(you’ll bring dishonor to yourself)"))
				if move not in available:
					raise TypeError("That wasn’t an option.")
			except:
				print("That wasn’t an option.")
			else:
				break

	if p_class == "priest":
		while True:
			try:
				move = int(input("How will you invoke your god?\n(1)Divine flame(A static point of fire blasts through the air dealing a set amount of damage each time)\n(2)Faith’s shield(You close your eyes as only the hand of your god protects you, although sometimes you catch em with their pants down and they don’t get there in time)\n(3)Healing light(divine energy suffuses your body mending wounds)\n(4)Pee your pants(This isn’t exactly a divine spell but it wouldn’t be the first time)"))
				if move not in available:
					raise TypeError("That wasn’t an option.")
			except:
				print("That wasn’t an option.")
			else:
				break
	return move
def move_effect(player_class, decision):
	if player_class == "sorcerer":
		if decision == 1:
			fire = random.randint(1,30)
			mhp -=fire




def classes (which):
    if which == 1:
        return "sorcerer"
    if which == 2:
        return "assassin"
    if which == 3:
        return "knight"
    if which == 4:
        return "priest"
    
def difficulty(difficult):
	if difficult == 1:
		monster = "wolf"
	if difficult == 2:
		monster = "bear"
	if difficult == 3:
		monster = "dark knight"
	return monster

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
    
           
        

available = [1,2,3,4]
options = [1,2,3]

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

decision  = p_turn(p_class)


while True:
	try:
		difficult = int(input("What difficulty — 1, 2, or 3: "))
		if difficult not in options:
			raise TypeError("that wasn’t an option.")
	except:
		print("That wasn’t an option")
	else:
		break

monster = difficulty(difficult)

if monster == "wolf":
	mhp =25
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



	
print(f"You are a {p_class} and your abilities are." )
for i in powers:
    print(i)

print(f"You are fighting a {monster}!")

if p_class == "sorcerer":
    php = 30
if p_class == "assassin":
    php = 25
if p_class == "knight":
    php = 45
if p_class == "priest":
	php = 25


while mhp > 0 and php > 0:
    if p_class == "sorcerer":
        ac = random.randint(10, 13)
        attack = 3
    if p_class == "assassin":
        ac = random.randint(15, 17)
        attack = 10
    if p_class == "knight":
        ac = random.randint(16, 18)
        attack = 8
    if p_class == "priest":
        ac = random.randint(9, 12)
        attack = 0


    enemy = m_turn(monster)




