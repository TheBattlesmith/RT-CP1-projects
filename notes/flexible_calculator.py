# Roman Torres, period 1, flexible calculator
import math

# Function for the different operations you can perform 
def equations(op, *args):

    if op == "sum":
        added = sum(args[0])
        return added
    elif op == "average":
        num = 0
        for i in args[0]:
            num += i
        total = num/len(args[0])
        return total
    elif op == "min":
        minimum = min(args[0])
        return minimum
    elif op == "max":
        maximum = max(args[0])
        return maximum
    elif op == "product":
        product = math.prod(args[0])
        return product


while True:

    # Lists for stupid proofing
    agreement = ["yes", "y", "yep"]
    operations = ["sum","average","min","max", "product"]
    finished = ["yes", "y", "no", "n"]

    # Lists for the inputed numbers
    plugin = []


    # While loop to get the desired numbers from user and stupid proof
    while True:
        try:
            numbers = float(input("\nWhat number would you like to add to your equation? "))
        except:
            print("That isn't a number.")
        else:
            plugin.append(numbers)
            sofar = str(plugin)
            print(f"So far, your numbers are ", (sofar))
            done = input("\n\nWould you like to continue? (Y/N): \n\n").lower().strip()
            if done not in agreement:
                break

    # Stupid proof while loop to get the operation from the user
    while True:
        try:
            operation = input("What operation do you want to preform on your chosen numbers? \nSum\nAverage\nMax\nMin\nProduct\n\n").lower().strip()
            if operation not in operations:
                raise TypeError("that wasn't an option")
        except:
            print("that wasn't an option")
        else:
            if operation in operations:
                break

    # Calling the function to get the values
    result = equations(operation, plugin)

    # Printing the final result
    print(f"Based on your choices, the answer to your question is: {result}")

    # Asking if the user wants to leave
    while True:
        try:
            done = input("\nWould you like to work a different equation? (y/n) --- ").lower().strip()
            if done not in finished:
                raise TypeError("That wasn't an option.")
        except:
            print("That wasn't an option")
        else:
            break
    if done == "no" or done == "n":
        print("Okay, goodbye!")
        break