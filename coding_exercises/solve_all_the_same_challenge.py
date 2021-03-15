from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """Check if all items in the list `elements` are the same."""
    if not elements or len(elements) == 1:
        return True
    previous = elements[0]
    for item in elements[1::]:
        if item == previous:
            continue
        else:
            return False
    return True


print(all_the_same([]))    # True
print(all_the_same([1, 1, 1]))    # True
print(all(['a', 'a', 'a']))    # True
print(all_the_same([1]))    # True
print(all_the_same([1, 2, 1]))    # False
