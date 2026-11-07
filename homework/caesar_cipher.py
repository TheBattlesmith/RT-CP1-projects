# Roman Torres, period 1, Ceasar Cipher

# place the program in a while loop so that the user can rerun without having to reload
while True:


# Function written to encode the message
    def encode():

        global cipher
        global encoded
        global encrypted
        encoded = []
        for i in cipher:

                NL = ord(i)
                new_index = NL + 2

                letter = chr(new_index)
                encoded.append(letter)
        encrypted = ''.join(encoded)
        return encrypted




# Fuction written to decode the message
    def decode():
        global alphabet
        global decoded
        global decrypted
        decoded = []
        for i in cipher:

                NL = ord(i)
                new_index = NL - 2

                letter = chr(new_index)
                decoded.append(letter)
        decrypted = ''.join(decoded)
        return decrypted


            




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
            
# Calling function to make the output if the user wants to encrypt
    if which == 1:
        encode()
        print("Your encrypted message is: \n")
        print(encrypted, "\n")
# Calling function to make the output if the user wants to decrypt
    elif which == 2:
        decode()
        print("Your decrypted message is: \n")
        print(decrypted, "\n")

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