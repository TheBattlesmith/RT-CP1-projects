# Roman Torres, period 1, Password Strength Checker Code

PassStrength = "Horrible"


password = input("What is your password (white space will not be included): ").strip()







capitals = password.upper()
small_let = password.lower()

strength = 0
lowercase = "No"
length = "No"
uppercase = "No"
integers = "No"
special = "No"

Sp_char = ["!","@","#","$","%","^","&","*",";",":","-","_","+","=","?","/",".",">","<",","]



for i in password:
    if i.isnumeric():
        integers = "Yes"
        strength += 1
        break

for i in password:
    if i in Sp_char:
        special = "Yes"
        strength += 1
        break


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



print(f"Integers included: {integers}\nUppercase included: {uppercase}\nLength greater than 7 {length}\nLowercase included: {lowercase}\nSpecial characters included: {special}\n\nOverall password strength---{strength}---{PassStrength}")


