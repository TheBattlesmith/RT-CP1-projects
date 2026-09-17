# Roman Torres
# 1st period
# Debugging with the debugger

# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) # I changed quantity to int

total = int(price * quantity)

discounted_total = total - (total * 0.10) # I changed the equation to actually match what a ten percent discount would look like

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) # I changed SnackName to match the variable located on line 9
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total)) # I changed price to discounted total in order to get the total price before tax
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # parenthese was missing