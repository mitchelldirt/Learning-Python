name = input("What is your name? ")
age = int(input("what is your age? "))

if 18 <= age <= 30:
    print("Hello {}, welcome to the holiday!".format(name))
else:
    print("Sorry, unfortunately you aren't allowed into the holiday.")
