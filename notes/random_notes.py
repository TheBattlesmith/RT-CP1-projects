import random

#function a named group of programing instructions that preforms a task

#arguments are the values you give a function when you call it - random.randint(5,6) - seperate with a comma

#return the value a function sends back after running

#random.randint(low, high) this returns a random high or low int

# random.randrange(start, stop, step) - a random whole number from a range, similar to the range() function works - the stop value is not included and you can use step to only land on certain   

#module / library a collection of pre-written code called using the import statement



beans = random.randint(1, 100)

print(beans)

fruits = ["apple", "banana","cherry"]





#choice function for lists

choice = random.choice(fruits)
print(f"random fruit: {choice}")





# Random.randrange() - start number , stop point not included[line 11], counting by step number

pens = random.randrange(1, 15, 3)

print(pens)


#random.random() - no arguments gives a random decimal between 0 and 1     the :.2 doesn't change the variable it only ensures that it looks right

percent = random.random()

print(f"You have a {percent:.2} grade.") 



