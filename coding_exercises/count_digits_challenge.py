def count_digits(text: str) -> int:
    i = 0
    for digits in text[::1]:
        if digits.isnumeric():
            i += 1
        else:
            continue
    return i


print(count_digits("123"))  # ANSWER WILL BE 3
print(count_digits("Hello1 World2 The3 Answer4 Is5 Six6"))  # ANSWER WILL BE 6
print(count_digits("1234567 hi8"))  # ANSWER WILL BE 8
