# Roman Torres, period 1, Ceasar Cipher


def decode():
    global alphabet
    global encoded
    global decoded
    decoded = []
    for i in encoded:
        if i in alphabet:
            NL = alphabet.index(i)
            new_index = NL - 2
            if new_index < 26:
                new_index = new_index + 26 - 2
            letter = alphabet[new_index]
            decoded.append(letter)
        else:
            continue

        

def encode():
    global alphabet
    global cipher
    global encoded
    encoded = []
    for i in cipher:
        if i in alphabet:
            NL = alphabet.index(i)
            new_index = NL + 2
            if new_index > 26:
                new_index = new_index - 26 + 2
            letter = alphabet[new_index]
            encoded.append(letter)
        else:
            continue


def format():
    global index_list 
    global formating
    global grouping
    global new_word
    formating = cipher.split()
    index_list = []
    new_word = []
    for i in formating:
        grouping = len(str(formating.index(i)))
        index_list.append(grouping)
        new_word.append(grouping)


        





alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v","w","x","y","z"]


cipher = input("Please enter your desired message: ")




encode()

print(*encoded)

decode()

print(*decoded)