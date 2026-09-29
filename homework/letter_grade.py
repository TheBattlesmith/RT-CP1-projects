# Roman Torres, What is my Grade --- period 1






while True:
    try:
        grade = float(input("Please input your current grade percentage: "))
        if grade > 100 or grade < 0:
            raise TypeError ("That's not a grade!")
    except:
        print("That is not a score, please try again.")
    else:
        break

while True:
    try:
        extra = float(input("Please input extra credit percentage. If none, type 0: "))
    except:
        print("That's not a valid score.")
    else:
        break



if extra == 0:
    grade_av = grade 
if extra > 0:
    grade_av = grade + extra



if grade_av < 60:
    score = "E/F"
elif grade_av <= 62:
    score = "D-"
elif grade_av <= 66:
    score = "D"
elif grade_av <= 69:
    score = "D+"
elif grade_av <= 72:
    score = "C-"
elif grade_av <= 76:
    score = "C"
elif grade_av <= 79:
    score = "C+"
elif grade_av <= 82:
    score = "B-"
elif grade_av <= 86:
    score = "B"
elif grade_av <= 89:
    score = "B+"
elif grade_av <= 92:
    score = "A-"
else:
        score = "A"





print(f"Your grade is {grade_av}% which is a/an {score}")