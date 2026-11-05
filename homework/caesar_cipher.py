# Roman Torres, period 1, Ceasar Cipher
while True:

    def decode():
        global alphabet
        global encoded
        global decoded
        decoded = []
        for i in encoded:

                NL = ord(i)
                new_index = NL - 2

                letter = chr(new_index)
                decoded.append(letter)

        return decoded

            

    def encode():
        global alphabet
        global cipher
        global encoded
        encoded = []
        for i in cipher:

                NL = ord(i)
                new_index = NL + 2

                letter = chr(new_index)
                encoded.append(letter)

        return encoded





    cipher = input("Please enter your desired message: ").lower()

    available = [1,2]

    while True:
        try:
            which = int(input("Would you like to \nEncrypt (1)\nOr decrypt(2)\n\nThis message? "))
            if which not in available:
                   raise TypeError("---That wasn't an option---")
        except:
             print("---That wasn't an option---")
        else:
             break
            

    if which == 1:
        encode()

        print(*encoded)

    if which == 2:
        decode()

        print(*decoded)