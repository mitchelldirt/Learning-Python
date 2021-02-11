def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    answer = text.replace(".", " ")
    answer = answer.replace(",", " ")
    answer = answer.split()
    return answer[0]


print(first_word("Hello.World, yuh"))