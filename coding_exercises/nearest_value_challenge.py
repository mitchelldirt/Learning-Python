def nearest_value(values: set, one: int) -> int:
    sorted_values = sorted(values)
    difference_list = []
    for x in sorted_values[::1]:
        if x < one:
            difference = one - x
            difference_list.append(difference)
        if x > one:
            difference = x - one
            difference_list.append(difference)
        if x == one:
            return x
    min_one = difference_list.index(min(difference_list))
    return sorted_values[min_one]

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))