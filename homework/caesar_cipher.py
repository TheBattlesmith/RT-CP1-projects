# Roman Torres, period 1, Ceasar Cipher


def decode():
    global alphabet
    global cipher
    global decoded
    decoded = []
    for i in cipher:
        if i in alphabet:
            NL = alphabet.index(i)
            new_index = NL - 2
            letter = alphabet[new_index]
            decoded.append(letter)
        else:
            continue
        

def encode():
    global alphabet

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v","w","x","y","z"]


cipher = input("Please enter your desired message: ")





decode()

print(*decoded)