# Roman Torres, Interactive Introduction Program Code

name = input("Hello there, what is your name? ")

hobby = input(f"nice to meet you, {name}. what do you enjoy to do? ")

home = input(f"{hobby}, eh, can't say I've ever done that before. Where do you live? ")







while True:
    try:
        age = int(input(f"Never heard of, {home}, before, I'm from... somewhere else. How old are you? "))
    except:
        print("that's not a number")

    else:
        break


if age >= 100:
    print("What!!!! HOW?!?!")
if age <= 20:
    print("okay, so not too old then. ")
if age < 100 and age > 20:
    print("Ah,so you're an adult then")
