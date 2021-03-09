import duck_test_modified

flock = duck_test_modified.Flock()
donald = duck_test_modified.Duck()
daisy = duck_test_modified.Duck()
duck3 = duck_test_modified.Duck()
duck4 = duck_test_modified.Duck()
duck5 = duck_test_modified.Duck()
duck6 = duck_test_modified.Duck()
duck7 = duck_test_modified.Duck()
percy = duck_test_modified.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
