numbers = range(1, 101)
for fizz_buzz in numbers:
    if fizz_buzz % 15 == 0:
        print('fizzbuzz')
    elif fizz_buzz % 3 == 0:
        print('fizz')
    elif fizz_buzz % 5 == 0:
        print('buzz')
    else:
        print(fizz_buzz)
