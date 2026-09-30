# Roman Torres


# List --- a complex data type that stores an ordered, changeable collection  of items, written inside square brackets.

# Complex data type --- a data type that can hold multiple values

# Lists can hold eny data type --- strings, ints, floats etc

# Index --- lists and tuples are ordered so that each item has a position starting at 0

# .append(value) --- adds an item to the end of the list

# .insert(index, value) --- adds an item at a specific position, shifting everything after it over one

# .extend(list) --- adds all items from one list to another list one at a time

# .remove(value) --- removes the first item in the list that matches the value

# .pop(index) --- removes an item from a list and returns it so you can use that value afterward. if no index given, it removes the last one




siblings = ["Amaia", "Kayla", "Cersie", "Mercy"]

print(siblings[2])


# Unpacking operator must be independent
print(*siblings)


print(f"My older sister is {siblings[0]}")

# negative flips the list
print(f"the youngest is {siblings[-1]}")

length = len(siblings)

siblings.append("Sadie")
print(*siblings)

siblings.insert(1, "Roman")
print(*siblings)



siblings.extend(["Talmadge", "Amon"])
print(*siblings)

siblings.remove("Roman")
print(*siblings)


siblings.pop(5)
print(*siblings)



# tuple --- stores an ordered, unchangeable collection of items written in parentheses. it is immutable

subjects = ("english,", "SS,", "Rogue,", "Blaze wielding,")




print(subjects[0])
print(*subjects)


# Set --- complex data type that stores an unordered (no index) collection of unique items (no duplicates) written in curly brackets {} --- you can find the length though

beans = {"black", "pinto", "brown", "pinto"}

beans.add("green")

beans.update({"pinkbeans", "jellybeans"})

beans.remove("pinkbeans")
print(*beans)


# you can convert lists, sets, and tuples

yum = tuple(beans)

kids = set(siblings)

lessons = list(subjects)

lessons.append("murder,")
print(*lessons)