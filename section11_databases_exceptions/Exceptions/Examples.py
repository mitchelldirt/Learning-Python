def factorial(n):
    # n! can also be defined n * n - 1
    """Calculates n recursively."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    print(factorial(int(input("Please enter a number: "))))

# You can use multiple exceptions in the same except statement.
except (RecursionError, ZeroDivisionError):
    print("This program cannot calculate factorials that large")

# You should use separate except clauses like below instead of the example above.
except ZeroDivisionError:
    print("You cannot divide by zero")

print("program terminating")