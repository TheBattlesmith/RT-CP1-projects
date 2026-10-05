# Roman Torres, Multiplication Table, period 1



multiplier = 0

for i in range(1, 13):
    multiplier += 1
    for i in range(multiplier, 13 * multiplier + 1, multiplier):
        print(i, end = "\t")
    print("\n")

