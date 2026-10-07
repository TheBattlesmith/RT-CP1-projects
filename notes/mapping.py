# Mapping: taking an existing list, doing the same operation to every item in it, and building a brand new list out of the results - the original list is left unchanged 

# Accumulator Pattern: a common technique where you start with an empty list, then use a for loop to add one new item to it during each pass - "accumulating" the results one at a time.

#Mapping is really the accumulator pattern with one extra step: instead of just copying each item into the new list, you transform it first (like doubling a number, or making a string uppercase) before adding it

#The original list used for mapping is never changed — you always end up with two separate lists: the original, and the new transformed one

import math


def times(number):
    return number *2

numbers = range(1,6)

multiplied_numbers = map(times, numbers)

print(*list(multiplied_numbers))


new_numbers = []

for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)

siblings = ["Amaia", "Kayla", "Cersei", "Mercy"]

length = list(map(len, siblings))
print(*length)


def product(complete):
    return complete * group

group = []

print(math.fractorial(5))