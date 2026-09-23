# RT Boolean Notes

# primitive data types: booleans, integers, floats, and strings

# Boolean examples
win = False

admin = True

# comparison operators: <, >, >=, <=, ==, !=, !>, !<,

age = int(input("how old are you? "))

if 18 < age: # 18 < age: is a boolean equation
    print("You are an an adult")


# you can assign anything into a boolean, only zero in ints will return false, and all strings are true unless they're empty.

print(bool(age))