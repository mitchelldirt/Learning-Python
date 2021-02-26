from collections import Counter


def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.
    data_new = []
    counter = Counter(data)
    if len(counter) == len(data):
        return []
    if len(counter) == 1:
        return data
    else:
        for item in data:
            if data.count(item) > 1:
                data_new.append(item)
    return data_new


print((checkio([1, 2, 3, 1, 3])))
