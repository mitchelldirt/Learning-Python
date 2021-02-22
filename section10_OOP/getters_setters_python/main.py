from enemy import Enemy, Troll, Vampire, VampireKing
import random

ugly_troll = Troll("Pug")
print(ugly_troll)

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

brother.take_damage(24)
print(brother)

old_vampire = Vampire("Olga")
print(old_vampire)

young_vampire = Vampire("Kelcy")
print(young_vampire)

young_vampire.take_damage(7)
print(young_vampire)

old_vampire.take_damage(30)
print(old_vampire)

# while young_vampire.alive:
#         young_vampire.take_damage(1)

young_vampire._lives = 0
young_vampire._hit_points = 1
print(young_vampire)

king_of_vampires = VampireKing("Dracula")
print(king_of_vampires)
while king_of_vampires.alive:
    king_of_vampires.take_damage(random.randint(10, 40))
