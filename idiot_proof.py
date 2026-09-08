# Roman Torres, idiot proof assignment

#name

first_name = input("What is your first name? ").strip().title()
last_name = input("What is your last name? ").strip().title()


seperate_one = first_name.split()
seperate_two = last_name.split()

fixed_firstname = "".join(seperate_one).strip().title()
fixed_lastname = "".join(seperate_two).strip().title()

#phone number

while True:

    try:
        phone_number = (int(input("What is your phone number? ")))

    except:
        print("Please enter a valid phone number with no spaces")

    else:
        break


string_phone = str(phone_number)


first_phone = string_phone[0:3]
second_phone = string_phone[3:6]
third_phone = string_phone[6:10]

final_phone = first_phone + " " + second_phone + " " + third_phone

#GPA

while True:
    try:
        gpa_question = int(input("What is your GPA? "))
    except:
        print("That is not a valid GPA.")
    else:
        break


GPA = (round(gpa_question, 2))




print(final_phone)

print(fixed_firstname + " " + fixed_lastname)

print(GPA)