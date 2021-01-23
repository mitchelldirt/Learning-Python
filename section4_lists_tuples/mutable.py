computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"]

another_list = computer_parts
print(id(computer_parts))
print(id(another_list))

computer_parts += ["Mic"]
print(computer_parts)
print(id(computer_parts))
print(another_list)

a = b = c = d = e = f = another_list
print(a)
print("adding cream")
b.append("cream")
print(c)
print(d)
print(a)
print(computer_parts)


