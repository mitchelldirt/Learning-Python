# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     text_list = []
#     text = text.split()
#     text.join(text_list)
#     begin_index = text_list.index(begin)
#     end_index = text_list.index(end)
#     del text_list[begin_index:-1]
#     del text_list[end_index:1]
#     word = " "
#     return word.join(text_list)
#
#
#
#
# print(between_markers('What is >apple<', '>', '<'))

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    b = text.index(begin) + len(begin) if begin in text else 0
    e = text.index(end) if end in text else len(text)
    return text[b:e]

print(between_markers('What is >apple<', '>', '<'))