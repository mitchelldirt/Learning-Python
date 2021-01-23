def multiply(x: float, y: float) -> float:
    """
    The multiply function can use any sequence type.

    :param x: User selected value
    :param y: User selected value
    :return: The product of 'x * y'.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Checks if a `str` is a palindrome or not.

    The function ignores whitespace, capitalisation, and
    punctuation in the sentence

    :param string: A string that the user will need to provide.
    :return: A boolean value for the string based on whether it's a
        palindrome of not.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence()

