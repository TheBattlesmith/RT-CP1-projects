# Roman Torres, What is my Grade --- period 1

while True:
    try:
        grade = float(input("Please input your current grade percentage: "))
    except:
        print("That is not a score, please try again.")
    else:
        break


if grade < 60:
    score = "E/F"
elif grade <= 63.5:
    score = "D-"
elif grade <= 66.5:
    score = "D"


print(f"Your grade is {grade}% which is an {score}")