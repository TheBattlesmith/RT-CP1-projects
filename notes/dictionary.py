
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

print(car)