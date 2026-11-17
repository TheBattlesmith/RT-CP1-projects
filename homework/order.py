# Roman Torres, period 1, order up

def final_p (list):
    final = 0
    for i in list:
        final += i

def sd (i):
    if i == 1:
        return 7
    elif i == 2:
        return  9
    elif i == 3:
        return  3
    else:
        return 793

def md (i):
    if i == 1:
        return 1
    elif i == 2:
        return 12
    elif i == 3:
        return 10
    else:
        return 5000

def dd (i):
    if i == 1:
        return  200
    elif i == 2:
        return 300
    elif i == 3:
        return  1
    else:
        return 250

def so (i):
    if i == 1:
        return "Pinto beans"
    elif i == 2:
        return "Black beans"
    elif i == 3:
        return "Green beans"
    else:
        return "Chili"

def mo (i):
    if i == 1:
        return "French croissant"
    elif i == 2:
        return "Baked potato"
    elif i == 3:
        return "JCW's sandwich"
    else:
        return "Steak"

def do (i):
    if i == 1:
        return "Orange juice"
    elif i == 2:
        return "Water"
    elif i == 3:
        return "Blood"
    else:
        return "Lemonade"


drinks = {
    "Orange juice": 200,
    "Water": 300,
    "Blood": 1,
    "lemonade": 250
}
main = {
    "French Croissant": 1,
    "Baked potato": 12,
    "JCW's sandwich (not stolen)": 10,
    "steak": 5000
}
sides ={
    "Pinto beans": 7,
    "Black beans": 9,
    "Green beans": 3,
    "Chili": 793
}

# Lists
stupid = [1,2,3,4]
total = []
choices = []

# Getting requested drink

print("what would you like to drink? (Number input)\n")
option_d = 1

for i, g in drinks.items():
    print(f"{option_d}: {i} - price ${g}")
    option_d += 1
print("")

while True:
    try:
        drink = int(input("\n"))
        if drink not in stupid:
            raise TypeError("That wasn't an option")
    except:
        print("That wasn't an option.")
    else:
        break
drink_dish = dd(drink)
d_choice = do(drink)

total.append(drink_dish)
choices.append(d_choice)




print("What will be your main course? (Number input) \n")
option_m = 1

for i, g in main.items():
    print(f"{option_m}: {i} - price ${g}")
    option_m += 1
print("")

while True:
    try:
        main = int(input("\n"))
        if main not in stupid:
            raise TypeError("That wasn't an option")
    except:
        print("That wasn't an option.")
    else:
        break
main_dish = md(main)
m_choice = mo(main)

total.append(main_dish)
choices.append(m_choice)


print("What do you want as your side dishes? (Number input) [choose 2]")
option_s = 1

for i, g in sides.items():
    print(f"{option_s}: {i} - price ${g}")
    option_s += 1

for i in range(2):
    while True:
        try:
            side = int(input("\n"))
            if side not in stupid:
                raise TypeError("That wasn't an option")
        except:
            print("That wasn't an option.")
        else:
            break
    
    side_dish = sd(side)
    s_choice = so(side)
    total.append(side_dish)

    choices.append(s_choice)

numbers = 0
index = 0
for i in total:
    index += 2
    numbers += total.index(index)

print(numbers)
