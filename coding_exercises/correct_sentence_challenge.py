def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    list1 = []
    answer = ""
    for x in text:
        list1.append(x)
        if list1[0].islower():
            list1[0] = list1[0].upper()
    answer = answer.join(list1)
    if answer[-1] != ".":
        return (answer + ".")
    else:
        return answer


print(correct_sentence("hello"))
