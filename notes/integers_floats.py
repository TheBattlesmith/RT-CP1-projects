# int cuts decimal, float keeps decimals, round rounds decimal


fav = input("what is your favorite number: ")
pi = 3.14

print(f"{float(fav)**2} is {fav} squared!")

# the 2 makes it round to two decimal places
print(round(pi,2))
print(int(pi))

