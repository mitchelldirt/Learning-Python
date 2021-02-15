from datetime import date


def days_diff(a, b):
    """
    Function to grab the difference between two tuples of dates
    """
    return abs((date(*a) - date(*b)).days)


print(days_diff((2011, 12, 30), (2011, 1, 1)))
