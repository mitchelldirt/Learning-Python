from collections import Counter


def frequency_sort(items):
    """Sort the iterable by frequency that the elements show up"""
    result = [item for items2, c in Counter(items).most_common()
              for item in [items2] * c]
    return result


print(other([4, 6, 2, 2, 6, 4, 4, 4]))
