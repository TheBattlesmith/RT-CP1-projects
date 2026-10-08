# Roman Torres, Period 1, Fractorial Calculator
while True:
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


    if factorial > 1:
        for i in range(1, factorial):
            numbers.append(" x ")
            numbers.append(i)

        numbers.pop(0)
        numbers.append(f" x {factorial}")
        print(*numbers, end = " \t" )

        print(" = ", *finished)
    


    elif factorial == 1:
        print("1 = 1")
     
