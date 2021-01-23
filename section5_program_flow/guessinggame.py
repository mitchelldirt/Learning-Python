import random

highest = 1000
lowest = 1
answer = random.randint(lowest, highest)
# print(answer)   #TODO: Remove after testing

print("Please guess number between {} and {}: ".format(lowest, highest))
guess = int(input())

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
    guess = int(input())

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



