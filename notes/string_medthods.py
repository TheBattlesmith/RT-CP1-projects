# Notes      question, why is this code bad?
# String methods
    # methods do not change your variable it only fixes output unless placed on the variable
    # example function - len(sentence)  len = action sentence = object acted on
    # example method - sentence.lower() object before action




# Strip function removes white space


sentence = "the quick brown fox jumps over the lazy dog"


# replace  
fixed = sentence.replace("fox", "wolf")

print(fixed)



print(sentence.find("over"))




word = input("what word do you want: ").strip().lower() #this changes the variable because it's attached
new_word = input("what word should be in the sentence? ").strip().lower()
location = sentence.find(word)
new_sentence = sentence.replace(word, new_word)

first_name = input("what is your first name: ").strip().title()

last_name = input("what is your last name: ").strip().title()

# split seperates characters into lists

first_seperated = first_name.split()
seperated = last_name.split()

# join takes characters together

fixed = "".join(seperated)
last_fixed = "".join(first_seperated)

sentence[4:7]

split = (sentence.split())

print(split)


full_name = last_fixed.title() + " " + fixed.title()

print("Hello " + full_name.title())
print(full_name.isalpha()) # checks if the entire thing is characters
print(full_name.isnumeric()) # checks if the entire thing is numbers
print(full_name.isupper()) # checks if the entire thing is uppercase


# Add strip to all inputs in the future


print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.title())


# f strings




#Step: 0 Result list: [0]
#Step: 1 Result list: [1]
#Final output: [1]



# ord looks up the numeric value of the key typed
# chr gives us the opposite of ord

letter = input("Give me a letter: ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"your letter was {letter} now it is {new_letter}")

