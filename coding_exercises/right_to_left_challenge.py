def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    text = ','
    list1 = []
    for word in phrases:
        list1.append(word)
    return text.join(list1).replace("right", "left")


print(left_join(("right", "left", "bright aright", "right", "bright")))



# This is the code I was trying to use. Above is much clearer.

# if word == "left":
#     list1.append(word)
# elif word == "right":
#     list1.append("left")
# elif right in word:
#     word.replace("right", "left")
#     list1.append(word)
# else:
#     list1.append(word)