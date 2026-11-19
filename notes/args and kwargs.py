#Positional argument: a value matched to a parameter by its position in the call. The first value goes to the first parameter, the second to the second, and so on.

#Keyword argument: a value passed by name (greeting="Hi"), so the order doesn't matter

#Default parameter: a parameter with a value already set in the definition (greeting="Hello"). It is used if the caller doesn't provide one.

#*args: lets a function accept any number of positional arguments. Python collects the extra values into a tuple.

#**kwargs: lets a function accept any number of keyword arguments. Python collects them into a dictionary.

#The names args and kwargs are just a convention. What matters is the * and **.

#Order matters: when a function uses several kinds, parameters go in this order: regular parameters, default parameters, *args, then **kwargs


def hello(name ,*args):
    print(args)
    for first in args:
        print(f"Hello {first}, {name}!")


hello("Kayla", "Amaia", "Cersie")

hello("Torres", "Amaia")


def clean(type, data):
    if type == "str":
        return data.strip().lower()
    elif type == "int":
        return int(data)
    elif type == "float":
        return round(float(data), 2)
    elif type == "list":
        return str(f"{x}, " for x in data)
    elif type == "bool":
        return f"{data}"
    


print(clean(type ="list", data ="700984"))


def neat (**kwargs):
    if kwargs["type"] == "str":
        return kwargs["data"].strip().lower()
    if kwargs["type"] == "int":
        return int(kwargs["type"])
    if kwargs["type"] == "float":
        return round(float(kwargs["data"]), kwargs["decimals"])
    if kwargs["type"] == "list":
        return str(f"{x}, " for x in kwargs["data"])
    if kwargs["type"] == "bool":
        return f"{kwargs["data"]}"

print(neat(data = "utah", type = "str"))
print(neat(type = "float", data = "3.1415", decimals = 3))