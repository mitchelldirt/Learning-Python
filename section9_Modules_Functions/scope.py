def factorial(n):
    """calculate n! iteratively *NOT RECURSIVE*"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def fact(n):
    """Recursive version of factorial function"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    """F(n) = F(n-1) + F(n -2) *RECURSIVE*"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    """Much faster version of the fib function *NOT RECURSIVE*"""
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


print("\n" + "*" * 40 + " NON-RECURSIVE FACTORIAL FUNCTION " + ("*" * 40) + "\n")
for i in range(40):
    print(i, factorial(i))

print("\n" + "*" * 40 + " RECURSIVE FACTORIAL FUNCTION " + ("*" * 40) + "\n")
for i in range(40):
    print(i, fact(i))

print("\n" + "*" * 40 + " NON-RECURSIVE FIBONACCI FUNCTION " + ("*" * 40) + "\n")
for i in range(40):
    print(i, fib(i))

print("\n" + "*" * 40 + " RECURSIVE FIBONACCI FUNCTION " + ("*" * 40) + "\n")
for i in range(40):
    print(i, fibonacci(i))
