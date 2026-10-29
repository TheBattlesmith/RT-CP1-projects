# Roman Torres, period 1, Password Strength Checker Code


# User input

password = input("What is your password (white space will not be included): ").strip()




# Setting the values for most variables


capitals = password.upper()
small_let = password.lower()

PassStrength = "Horrible"

strength = 0
lowercase = "No"
length = "No"
uppercase = "No"
integers = "No"
special = "No"

# list of all available special characters
Sp_char = ["!","@","#","$","%","^","&","*",";",":","-","_","+","=","?","/",".",">","<",","]


# Checking for integers
for i in password:
    if i.isnumeric():
        integers = "Yes"
        strength += 1
        break

# Checking for special characters
for i in password:
    if i in Sp_char:
        special = "Yes"
        strength += 1
        break

# Checking the password length
if len(password) >= 8:
    strength += 1
    length = "Yes"

# Checking for lowercase letters
if password != capitals:
    strength += 1
    lowercase = "Yes"
# Checking for uppercase letters
if password != small_let:
    strength += 1
    uppercase = "Yes"



# Setting the value of the code's strength
if strength == 1 or strength == 2:
    PassStrength = "Weak"
if strength == 3:
    PassStrength = "Moderate"
if strength == 4:
    PassStrength = "Strong"
if strength == 5:
    PassStrength = "Very Strong"


# Final judgment output
print(f"Integers included: {integers}\nUppercase included: {uppercase}\nLength greater than 7: {length}\nLowercase included: {lowercase}\nSpecial characters included: {special}\n\nOverall password strength---{strength}---{PassStrength}")


