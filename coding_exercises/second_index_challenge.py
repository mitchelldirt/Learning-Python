def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    i = 0
    for thing in text:
        if thing == symbol:
            i += 1
    if i < 2:
        return None
    else:
        first_spot = text.index(symbol)
        return text.index(symbol, first_spot + 1)


print(second_index("hi", " "))
print(second_index("sims", "s"))
print(second_index("Hello human nice to meet you", "e"))

