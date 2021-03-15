def split_list(items: list) -> list:
    """Split `items` list into two lists. If length of `items` is odd the first list should be longer."""
    if not items:
        return [[], []]
    len_list = len(items)
    if len_list % 2 != 0:
        split_index = len_list // 2
        split_index += 1
    else:
        split_index = len_list // 2
    list1 = []
    list2 = []
    for x in items[0:split_index]:
        list1.append(x)
    for y in items[split_index::]:
        list2.append(y)
    return [list1, list2]


print(split_list([1, 2, 3, 4, 5]))  # [[1, 2, 3], [4, 5]]
print(split_list([1, 2, 3, 4]))    # [[1, 2], [3, 4]]
print(split_list([]))   # [[], []]
