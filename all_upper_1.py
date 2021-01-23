# def is_all_upper(text: str) -> bool:
#     if text == "" or text.isspace() or text.isnumeric() or text.isupper():
#         return True
#     if text.islower():
#         return False
#     else:
#         return False
#
#
# print(is_all_upper("AIO"))

def is_all_upper_2(text: str) -> bool:
    return text.upper() == text

print(is_all_upper_2("123"))