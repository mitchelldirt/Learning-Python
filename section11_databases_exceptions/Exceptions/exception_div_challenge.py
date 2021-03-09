import sys
# This is how you created the function.
def two_numbers():
    """Get input for x and y from user and perform x divided by y"""
    try:
        x = int(input("Please Enter A Number: "))
        y = int(input("Please Enter Another Number: "))
    except ValueError:
        return "Only integers please, no spaces or alphabetical characters"
    except EOFError:
        sys.exit(0)
    else:
        try:
            return f"{x} divided by {y} equals {x / y}"
        except ZeroDivisionError:
            return "No dividing by zero please"
        finally:
            print("The finally clause will always be output.")



print(two_numbers())


# This is the professors way of doing the function.
def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Only integers please, no spaces or alphabetical characters")
        except EOFError:
            sys.exit(1)
        finally:
            print("Finally clause is always outputted.")


first_int = getint("Please enter first number ")
second_int = getint("Please enter second number ")

try:
    print(f"{first_int} divided by {second_int} is {first_int / second_int}")
except ZeroDivisionError:
    print("Please don't use zero for your second number")
else:
    print("Division performed successfully!")


