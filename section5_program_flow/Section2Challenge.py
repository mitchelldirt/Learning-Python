choice = " -"
while choice != "0":
    if choice in "1234":
        print("You chose {}".format(choice))
    else:
        print("Please choose your options from the list below")
        print("1:\tThe Forest")
        print("2:\tThe Mountains")
        print("3:\tThe Beach")
        print("4:\tThe Ocean")
        print("0:\tExit")

    choice = input("Please choose a number from the list above ")
print("Good bye")