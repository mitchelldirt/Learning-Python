def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if not array:
        return 0
    else:
        return sum(array[::2]) * array[-1]


print(checkio([1, 3, 5]))