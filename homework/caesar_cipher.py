# Roman Torres, period 1, Ceasar Cipher




# Function written to encode the message
def encode():
    encoded = []
    for i in cipher:
        if i.isupper():
            start = 65
            new_index = chr((ord(i) - start - shift) % 26 + start)
            encoded.append(new_index)
        elif i.islower():
            start = 97
            new_index = chr((ord(i) - start - shift) % 26 + start)
            encoded.append(new_index)

        else:
            encoded.append(i)
        

        
        
    encrypted = ''.join(encoded)
    return encrypted




# Fuction written to decode the message
def decode():
    decoded = []
    for i in cipher:
        if i.isupper():
            start = 65
            new_index = chr((ord(i) - start + shift) % 26 + start) 
            decoded.append(new_index)
        elif i.islower():
            start = 97
            new_index = chr((ord(i) - start + shift) % 26 + start) 
            decoded.append(new_index)
        else:
            decoded.append(i)
         
    decrypted = ''.join(decoded)
    return decrypted




# place the program in a while loop so that the user can rerun without having to reload
while True:


# Getting user input for the text available to the program

    cipher = input("Please enter the message you want to encrypt/decrypt: ")
    print(" ")

    available = [1,2]
# Checking if the user wants to encrypt or decrypt
    while True:
        try:
            which = int(input("Would you like to encrypt or decrypt this message? \nFor encrypt input - (1)\nFor decrypt input - (2): "))
            if which not in available:
                   raise TypeError("---That wasn't an option---")
        except:
             print("---That wasn't an option---")
        else:
             print(" ")
             break

# Getting user input for the shift value
    while True:
        try:
            shift = int(input("Please enter the shift value integer you want to use: "))
        except:
             print("---That wasn't an option---")
        else:
             print(" ")
             break        
        

# Calling function to make the output if the user wants to encrypt
    if which == 1:
        print("Your encrypted message is: \n")
        print(encode(), "\n")
        
# Calling function to make the output if the user wants to decrypt
    elif which == 2:
        print("Your decrypted message is: \n")
        print(decode(), "\n")

# Checking whether the user wants to exit the program
    while True:
        try:
            exit = int(input("Would you like to exit this program? \nFor yes input - (1)\nFor no input any integer aside from 1: "))

        except:
             print("---That wasn't an option---")
        else:
             print(" ")
             break
# If the user wants to exit the program, this will break the loop
    if exit == 1:
        print("---Thank you for making use of this program---")
        break