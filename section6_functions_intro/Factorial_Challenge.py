def factorial(n: int) -> int:
    """
    Get the factorial value of `number`.
    :param number: Numbers in a given range (0, 36)
    :return: The factorial value
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


for i in range(36):
    print(i, factorial(i))
