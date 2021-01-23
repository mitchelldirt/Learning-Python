vegetables = {"broccoli": "A yucky green veggie",
              "carrot": "An orange log",
              "lettuce": "Food for cows",
              "mushroom": "The best on burgers",
              "radish": "What the hell is a radish"
              }

print(vegetables)

fruit = {"orange": "A sweet, orange, citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow, citrus fruit",
         "grape": "A small, sweet fruit growing in bunches",
         "lime": "A sour, green, citrus fruit"}

# print(fruit)
#
# vegetables.update(fruit)
# print(vegetables)
# fruit.update(vegetables)
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(vegetables)
print(nice_and_nasty)
print(vegetables)
print(fruit)