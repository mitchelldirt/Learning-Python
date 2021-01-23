# a = int(input("What is the value of a "))
# check = type(a)
# print(a,check)
#
# b = int(input("What is the value of b "))
# check = type(b)
# print(b,check)
#
# c = int(input("What is the value of c "))
# check = type(c)
# print(c,check)
#
# print(a + b - c)

#ACTUAL SOLUTION
# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)
