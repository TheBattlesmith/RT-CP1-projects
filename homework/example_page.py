#Roman Torres Variables notes

name = "Katie"

print("hello "+ name)

# reset variable

name ="peter"

print("Sorry I meant, "+ name)

#another variable example
age = 16

print("Wow you are, ", age)
print("Oh wait your birthday was yesterday?")
age += 1
print("so you are, ", age)

print("we did this on codespace")

# debugging is the process of removing errors from your code

#error types: 
# Syntax errors - you wrote it wrong, indentation error
# Logic errors - program runs but produces wrong result, because your steps are wrong
# Run time Errors - errors that happen when the code is running causing them to crash partway through
    #example
#fav_num = int(input("what is your favorite number: "))
#print(4 + fav_num)
    #the fix
while True:
    try:
        fav_num = int(input("what is your favorite number: "))
    except:
        print("that's not a number")
    else:
        break
print(4 + fav_num)


# PEMMDAS - parenthesis, exponents, multiplication, modules, division 

num = 3
num = num + 2        
num += 3        

num //= 3
print(f"after mod{num}")