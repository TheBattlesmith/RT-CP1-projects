
#Dictionary: a collection of key-value pairs. You look things up by key, like looking up a word in a real dictionary.

#Key: the label used to find a value. Keys must be unique and unchangeable (strings, numbers, and tuples work; lists do not).

#Value: the data stored with a key. It can be any type, including a list or another dictionary.

#Lists vs. dictionaries: a list finds items by position (nums[0]). A dictionary finds items by key (student["name"]).

#Duplicate keys: a key can only exist once. Assigning to an existing key replaces its value.

#KeyError: the error you get when you use d[key] and the key isn't there. d.get(key) avoids it.

#Nested dictionary: a dictionary stored as a value inside another dictionary. Use one pair of brackets per level: people["Sam"]["age"].

#Reference type: a dictionary is a complex (reference) data type, not a simple primitive like an int or a bool


car = {
    #Key     Value
    "make": "Jeep",
    "model": "Wrangler",
    "color": "silver",
    "year": 2023
}


keys = list(car.keys())
values = list(car.values())



print(values)
print(len(car))
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

for key in keys:
    print(f"{key} is {car[key]}")



# to remove
car.pop("color")


# prints keys
print(car)

# prints values
print(car["make"])

print(list(car.keys()))







avatar = {
    "water": {
        "Katara": "Water bender",
        "Sokka": "Leader",
    },
    "earth": {
        "Toph": "Earth bender"
    },
    "air": {
        "Aang": "Air bender"
    },
    "fire": {
        "Zuko": "Fire bender",
        "Iroh": "Fire GOAT",
        "Azula": "crazy",
    }

}


# Brackets near eachother for stacked lists
print(avatar["fire"]["Iroh"])

# Common problem Bumi doesn't exist

#print(avatar["earth"]["Bumi"])

print(avatar.get("earth").get("Bumi"))

# fix
