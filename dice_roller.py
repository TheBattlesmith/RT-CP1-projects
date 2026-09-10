# Roman Torres - dice roller project

import random


d4 = random.randint(1, 4)
d6 = random.randint(1,6)
d10 = random.randint(1,10)
d12 = random.randint(1,12)
d20 = random.randint(1,20)



options = ["d4", "d6", "d10", "d12", "d20", "D4", "D6", "D10", "D12", "D20"]
while True:
    try:
        option = input("which size dice do you want to roll? (D4, D6, D10, D12, D20): ")
        if option not in options:
            raise TypeError("that wasn't a choice.")
        else:
            break
            
    except:
        print("that's not a die!")
    else:
        break
   







if option == "d4" or "D4":
    print(f"your roll is: {d4}")

else:
    print("")

    

if option == "d6" or "D6":
    print(f"your roll is: {d6}")
else:
    print("")
if option == "d10" or "D10":
    print(f"your roll is: {d10}")
else:
    print("")
if option == "d12" or "D12":
    print(f"your roll is: {d12}")
else:
    print("")
if option == ["d20", "D20"]:
    print(f"your roll is: {d20}")
else:
    print("")