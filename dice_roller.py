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
        option = str(input("which size dice do you want to roll? (D4, D6, D10, D12, D20): "))
        if option not in options:
            raise TypeError("that wasn't a choice.")
        else:
            break
            
    except:
        print("that's not a die!")
    else:
        break
   







while options == "d4" or "D4":
    print(f"your roll is: {d4}")
    break

    

while options == "d6" or "D6":
    print(f"your roll is: {d6}")
    break

while options == "d10" or "D10":
    print(f"your roll is: {d10}")
    break

while options == "d12" or "D12":
    print(f"your roll is: {d12}")
    break

while options == "d20" or "D20":
    print(f"your roll is: {d20}")
    break
