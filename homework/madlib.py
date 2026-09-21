#Roman Torres - madlib project - 1st period

ml1 = input("please input a noun: ")
ml2 = input("please input a past tense verb: ")


while True:
    try:
        ml3 = (input("please input a number: "))
    
    except:
        print("that's not a number")
    else:
        break

ml4 = input("please input a past tense verb: ")
ml5 = input("please input a present tense verb: ")
ml6 = input("please input an adjective: ")




message = "a " + ml1 + " wielding ninja " + ml2 + " on a building " + ml3 + " times. After that, he " + ml4 + " and hit someone with his " + ml1 +  " weapon. That person started to " + ml5 + " and became a/an " + ml6 + " person, who beat the ninja and made him " + ml5 + " too."


print(message)