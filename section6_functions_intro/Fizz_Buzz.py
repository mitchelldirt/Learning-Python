def fizz_buzz(x: int) -> str:
    """
    Play Fizz buzz

    :param x: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if x % 15 == 0:
        return "fizzbuzz"
    elif x % 3 == 0:
        return "fizz"
    elif x % 5 == 0:
        return "buzz"
    else:
        return str(x)


input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    # players_answer = correct_answer
    if players_answer != correct_answer:
        print("You lose. The correct answer was {}"
              .format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))