# Roman Torres, period 1, flexible calculator
import math

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

agreement = ["yes", "y", "yep"]
plugin = []
operations = ["sum","average","min","max", "product"]
while True:
    try:
        numbers = float(input("What number would you like to add to your equation? "))
    except:
        print("That isn't a number.")
    else:
        plugin.append(numbers)
        sofar = str(plugin)
        print(f"So far, your numbers are ", (sofar))
        done = input("\n\nWould you like to continue? (Y/N): \n\n").lower().strip()
        if done not in agreement:
            break


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


result = equations(operation, plugin)

print(f"Based on your choices, the answer to your question is: {result}")