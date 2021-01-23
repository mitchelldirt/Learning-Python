albums = [("Welcome to my nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("NightFlight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1986),
          ]
print(len(albums))


for (name, artist, year) in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))w


table = ("Coffee Table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)
