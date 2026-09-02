


sentence = "the quick brown fox jumps over the lazy dog"

print(sentence)

# index begins at zero
# the + 1 makes it counting numbers
print(sentence.find("b")+1)


# Slicing strings
#index the position of a character within a string 
# doesn't goes to end point and stops. doesn't include end point
print(sentence[10:15])

word = input("what word do you want? ")
start = sentence.find(word)
length = len(word)


print(sentence[start: start + length])
