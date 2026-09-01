# Roman Torres, Average Grade assignment

print("please input your grades below.")


while True:
    try:
        period1 = float(input("period 1: "))
        period2 = float(input("period 2: "))
        period3 = float(input("period 3: "))
        period4 = float(input("period 4: "))
        period5 = float(input("period 5: "))
        period6 = float(input("period 6: "))
        period7 = float(input("period 7: "))
    except: 
        print("that's not a number") 
    else:
        break

average = {float(period1) + (period2) + (period3) + (period4) + (period5) + (period6) + (period7)}

print(f"your overal average grade is: {round(average,2)}")    