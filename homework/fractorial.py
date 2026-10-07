# Roman Torres, Period 1, Fractorial Calculator

while True:
    try:
        fractorial = (int(input("please input a positive integer to recieve its fractorial value: ")))
        if fractorial <= 0:
            raise TypeError("---The inputed integer must be larger than zero---")
    except:
        print("--- That is not an available input, please input a valid number---")
    else:
        break


top = range(1, fractorial)

