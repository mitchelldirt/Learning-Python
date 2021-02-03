import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
list1 = []
str1 = " "
for x in s:
    if x != 0:
        list1.append(ord(x))
print(sum(list1) // len(list1))

