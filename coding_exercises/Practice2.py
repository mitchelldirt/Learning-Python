from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if not items:
        return items
    if border not in items:
        return items
    else:
        x = border
        if x in items:



print(list(remove_all_before([1, 2, 2, 4, 5], 2)))


# split up items
# .join it together in an empty string
# Make it an integer
# Remove everything before the border integer (Or take everything after and including the border integer)
# Return it as a list with ',' as a separator

