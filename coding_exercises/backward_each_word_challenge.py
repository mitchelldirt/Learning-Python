def backward_string_by_word(text: str) -> str:
    list2 = []
    res = [i for j in text.split(' ') for i in (j, ' ')][:-1]
    for word in res:
        list2.append(word[::-1])
    return ''.join(list2)


def backward_string_by_word2(text: str) -> str:
    return ' '.join(x[::-1] for x in text.split(' '))


print(backward_string_by_word("Hello  World"))
print(backward_string_by_word2("Hello  World"))