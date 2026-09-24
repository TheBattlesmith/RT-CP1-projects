# Roman Torres, User Sign In, period 1


user_name = ["Miss. LaRose", "roman.torres"]

password_answer = "Beans!"




while True:

    try:
        username = input("Please input your username: ")
        if username not in user_name:
            raise TypeError ("That is incorrect. Please input a valid username.")

    except:
        print("that is incorrect. Please try again.")
    else:
        break
password = input("Please input your password ")