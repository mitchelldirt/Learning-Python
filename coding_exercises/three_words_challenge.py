def checkio(words: str) -> bool:
    """
    Checks to see if there are 3 words in a row in `words`.
    :param words: User provided string.
    :return: True if 3 words in a row. False if not.
    """
    count = 0
    for word in words.split():
        if count == 3:
            break
        if word.isalpha():
            count += 1
        if word.isnumeric():
            count = 0
    return False if count < 3 else True


print(checkio("a a a"))  # TRUE
print(checkio('1 1 a a 1 1'))  # FALSE
print(checkio('1 a a a 1'))  # TRUE
print(checkio("one two 3 four five 6"))  # FALSE
