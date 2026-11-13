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
    



