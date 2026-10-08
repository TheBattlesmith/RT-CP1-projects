# Roman Torres, Period 1, Fractorial Calculator

import math


while True:
    try:
        factorial = (int(input("please input a positive integer to recieve its fractorial value: ")))
        if factorial <= 0:
            raise TypeError("---The inputed integer must be larger than zero---")
    except:
        print("--- That is not an available input, please input a valid number---")
    else:
        break


finished = []

finished.append(math.factorial(factorial))

numbers = []



for i in numbers:
    print(*numbers, end = " x \t" )
print(*finished)
  



