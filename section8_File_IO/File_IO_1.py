# jabber = open("C:/Users/Mitchell/Desktop/sample.txt",'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# with open("C:/Users/Mitchell/Desktop/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
# with open("C:/Users/Mitchell/Desktop/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()
#
# with open("C:/Users/Mitchell/Desktop/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# TODO: Hey fix this wack ass code
# for line in lines:
#     print(line, end='')
with open("C:/Users/Mitchell/Desktop/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

    with open("C:/Users/Mitchell/Desktop/sample.txt", 'r') as jabber:
        lines = jabber.read()
    print(lines)

    for line in lines[::-1]:
        print(line, end='')