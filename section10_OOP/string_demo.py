# a standard string
a_string = "this is \na string split\t\tand tabbed"
print(a_string)

# A raw string: ignores \t and \n and will print whatever is within the quotes.
raw_string = r"this is \na string split\t\tand tabbed"
print(raw_string)

# If we didn't have \t or \n this is what our strings would look like.
b_string = "this is" + chr(10) + "a split string" + chr(9) + chr(9) + "and tabbed"
print(b_string)

# If you use \f it will return the weird character: You can use a raw string instead.
backslash_string = "This is a blackslash \followed by some text"
print(backslash_string)

# You can also use two backslashes instead to get the same result.
backslash_string = "This is a backslash \\followed by some text"
print(backslash_string)

# This gives an error because the '\' character is an escape key.
error_string = r"this string ends with \"

#This fixes the issue above because it uses two backslashes.
error_string = r"this string ends with \\"
print(error_string)