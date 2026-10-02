# Roman Torres --- period 1 --- Shopping List manager


shop = [ ]

while True:
    action = input("would you like to: add, remove, show, or exit your shopping list? ").lower().strip()


    if action == "add":
        addition = input("What would you like to add: ")
        shop.append(addition.title().strip())

    elif action == "remove":
        remove = input("What would you like to remove: ").title().strip()
        if remove in shop:
            shop.remove(remove)
        else:
            print("That is not a removable item.")


    elif action == "show":
        see = set(shop)
        print("Your list is: \n")
        print(*see)
        shop = list(see)


    elif action == "exit":
        print("Thank you for shopping---\nHave a nice day!")
        break

