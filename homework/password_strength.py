# Roman Torres, period 1, Password Strength Checker Code

PassStrength = "Horrible"


password = input("What is your password (white space will not be included): ").strip()

final = len(password)+1

p_list = password.split()

capitals = password.upper()
small_let = password.lower()

strength = 0
lowercase = "No"
length = "No"
uppercase = "No"
integers = "No"
special = "No"

numbers = [0,1,2,3,4,5,6,7,8,9]
for i in range[0, final]:
    


if len(password) >= 8:
    strength += 1
    length = "Yes"

if password != capitals:
    strength += 1
    uppercase = "Yes"

if password != small_let:
    strength += 1
    lowercase = "Yes"



if strength == 1 or strength == 2:
    PassStrength = "Weak"
if strength == 3:
    PassStrength = "Moderate"
if strength == 4:
    PassStrength = "Strong"
if strength == 5:
    PassStrength = "Very Strong"



print(integers, uppercase, length, lowercase, PassStrength)


