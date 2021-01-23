import random


def get_integer(prompt):
    """
    Get an integer from standard input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


help(get_integer)

highest = 1000
lowest = 1
answer = random.randint(lowest, highest)
# print(answer)   #TODO: Remove after testing

print("Please guess number between {} and {}: ".format(lowest, highest))
guess = 0

#THIS IS THE NOT SO GOOD WAY TO TYPE THIS
# if guess == answer:
#     print("You got it first time")
# while guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     while guess > answer:
#         print("Please guess lower")
#         guess = int(input())
# if guess == answer:
#     print("Well done, you guessed it")

#THIS IS THE BETTER WAY TO TYPE THIS

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        if guess > answer:
            print("Please guess lower")



