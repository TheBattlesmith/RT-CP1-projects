# Roman Torres, idiot proof assignment


first_name = input("What is your first name? ").strip().title()
last_name = input("What is your last name? ").strip().title()


seperate_one = first_name.split()
seperate_two = last_name.split()

fixed_firstname = "".join(seperate_one).strip().title()
fixed_lastname = "".join(seperate_two).strip().title()


while True:

    try:
        phone_number = (int(input("What is your phone number? ")))

    except:
        print("Please enter a valid phone number")

    else:
        break












print(fixed_firstname + " " + fixed_lastname)
