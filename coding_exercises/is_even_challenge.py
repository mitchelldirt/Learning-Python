def is_even(num: int) -> bool:
    num_range = range(-1000, 1000, 2)
    return True if num in num_range else False


print(is_even(2))
print(is_even(5))
print(is_even(0))
print(is_even(-7))
print(is_even(-8))